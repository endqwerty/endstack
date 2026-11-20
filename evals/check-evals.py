#!/usr/bin/env python3
"""Lint evals/: every case's prompt.md and graders parse and use only known keys.

Usage: python3 evals/check-evals.py   (exit 1 on any problem)
Patterns are compiled with Python's re, and with JavaScript's RegExp when node is on PATH,
because the Claude arm grades with JavaScript and the Codex arm with Python.
"""
import json, os, re, shutil, subprocess, sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVALS = os.path.join(ROOT, "evals")
PROMPT_KEYS = {"name", "tags", "runs", "max_turns", "timeout_seconds", "allowed_tools", "disallowed_tools"}
RUNNER_KEYS = {"append_system_prompt", "model", "plugins"}
GRADER_KEYS = {
    "regex": ({"type", "pattern"}, {"flags", "match", "target", "weight"}),
    "file_exists": ({"type", "path"}, {"exists", "weight"}),
    "tool_used": ({"type", "tool"}, {"input_match", "min", "max", "weight"}),
    "llm": ({"type", "criteria"}, {"weight"}),
}
TARGETS = {"last_message", "trace", "files"}


def frontmatter(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n?(.*)", text, re.S)
    if not m:
        raise ValueError("no YAML frontmatter between --- lines")
    data = yaml.safe_load(m.group(1))
    if not isinstance(data, dict):
        raise ValueError("frontmatter is not a mapping")
    return data, m.group(2)


def check_prompt(case, path, skills, problems):
    fm, body = frontmatter(path)
    for k in sorted(set(fm) & RUNNER_KEYS):
        problems.append(f"{path}: {k} is set by the runner; remove it")
    for k in sorted(set(fm) - PROMPT_KEYS - RUNNER_KEYS):
        problems.append(f"{path}: unknown key {k}")
    if fm.get("name") != case:
        problems.append(f"{path}: name must be the folder name {case!r}")
    tags = fm.get("tags")
    if not isinstance(tags, list) or not tags:
        problems.append(f"{path}: tags must list the skills the case exercises")
    else:
        for t in tags:
            if t not in skills:
                problems.append(f"{path}: tag {t!r} is not a skill in skills/")
    for k in ("runs", "max_turns", "timeout_seconds"):
        if k in fm and (not isinstance(fm[k], int) or fm[k] < 1):
            problems.append(f"{path}: {k} must be a positive integer")
    if not body.strip():
        problems.append(f"{path}: empty prompt")
    if re.search(r"\bskills?\b", body, re.I):
        problems.append(f"{path}: the prompt mentions a skill; routing must pick it")


def check_grader(path, patterns, problems):
    g, _ = frontmatter(path)
    kind = g.get("type")
    if kind not in GRADER_KEYS:
        problems.append(f"{path}: type must be one of {', '.join(GRADER_KEYS)}")
        return
    required, optional = GRADER_KEYS[kind]
    for k in sorted(required - set(g)):
        problems.append(f"{path}: missing {k}")
    for k in sorted(set(g) - required - optional):
        problems.append(f"{path}: unknown key {k} for type {kind}")
    if kind != "regex":
        if kind == "llm" and g.get("criteria", "").count("?") != 1:
            problems.append(f"{path}: criteria must be one yes-or-no question")
        return
    target = g.get("target", "last_message")
    if isinstance(target, dict):
        if set(target) != {"source", "path"} or target.get("source") != "file":
            problems.append(f"{path}: a file target is {{source: file, path: <relative path>}}")
    elif target not in TARGETS:
        problems.append(f"{path}: target must be one of {', '.join(sorted(TARGETS))} or a file")
    match = str(g.get("match", "contains"))
    if not re.fullmatch(r"contains|not_contains|count:\d+", match):
        problems.append(f"{path}: match must be contains, not_contains or count:N")
    flags = g.get("flags", "")
    if not re.fullmatch(r"[imsu]*", flags):
        problems.append(f"{path}: flags must be a subset of i, m, s, u")
    try:
        re.compile(g.get("pattern", ""), (re.I if "i" in flags else 0) | (re.M if "m" in flags else 0) | (re.S if "s" in flags else 0))
    except re.error as e:
        problems.append(f"{path}: pattern does not compile in Python: {e}")
    patterns.append((path, g.get("pattern", ""), flags))


def check_js(patterns, problems):
    node = shutil.which("node")
    if not node or not patterns:
        return
    script = ("const ps=JSON.parse(require('fs').readFileSync(0,'utf8'));"
              "for(const [p,s,f] of ps){try{new RegExp(s,f)}catch(e){console.log(p+': pattern does not compile in JavaScript: '+e.message)}}")
    out = subprocess.run([node, "-e", script], input=json.dumps(patterns), capture_output=True, text=True)
    problems.extend(line for line in out.stdout.splitlines() if line)
    if out.returncode:
        problems.append("node failed: " + out.stderr.strip())


def main():
    skills = set(os.listdir(os.path.join(ROOT, "skills")))
    problems, patterns, cases = [], [], 0
    for case in sorted(os.listdir(EVALS)):
        base = os.path.join(EVALS, case)
        if not os.path.isdir(base) or case == "results":
            continue
        cases += 1
        prompt = os.path.join(base, "prompt.md")
        graders = os.path.join(base, "graders")
        try:
            check_prompt(case, prompt, skills, problems)
        except (OSError, ValueError, yaml.YAMLError) as e:
            problems.append(f"{prompt}: {e}")
        files = sorted(f for f in os.listdir(graders) if f.endswith(".md")) if os.path.isdir(graders) else []
        if not files:
            problems.append(f"{base}: no graders/*.md")
        for f in files:
            try:
                check_grader(os.path.join(graders, f), patterns, problems)
            except (OSError, ValueError, yaml.YAMLError) as e:
                problems.append(f"{os.path.join(graders, f)}: {e}")
    check_js(patterns, problems)
    for p in problems:
        print(os.path.relpath(p, ROOT) if os.path.isabs(p.split(":")[0]) else p)
    print(f"{cases} case(s), {len(patterns)} pattern(s), {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
