#!/usr/bin/env python3
"""Lint skills/: frontmatter, size, portability, links. Exit 1 on any problem."""
import os, re, sys

CORE = {"build", "babysit", "ship", "autopilot-stack", "autopilot-full", "verify"}
CORE_MAX = 2200      # bytes, SKILL.md of a core delivery skill
OTHER_MAX = 6000     # bytes, SKILL.md of any other skill; detail goes in references/
DESCRIPTION_MAX = 200  # characters; a visible description is paid on every request
POLICY = "agents/openai.yaml"  # Codex reads allow_implicit_invocation here; false keeps a skill out of its catalog
FORBIDDEN = [
    (r"`(?:gh|git|npm|bun|npx|pnpm|yarn|curl)\b[^`]*`", "command in backticks"),
    (r"(?<![\w-])(?:Task|Read|Edit|Bash|Grep|TodoWrite) tool\b", "harness tool name"),
    (r"/(?:loop|schedule)\b", "harness slash command"),
    (r"\b(?:claude|anthropic|codex|openai|gpt|grok|opus|sonnet|haiku|gemini|composer)\b", "model or provider name"),
    (r"\b(?:cursor|t3 ?code)\b", "harness name"),
    (r"~/\.[a-z]|\.mdc\b", "harness config path"),
]


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        k, sep, v = line.partition(":")
        if sep and not line.startswith(" "):
            fm[k.strip()] = v.strip().strip("\"'")
    return fm


def check(root, only=None):
    problems = []
    skills = os.path.join(root, "skills")
    for name in sorted(os.listdir(skills)):
        d = os.path.join(skills, name)
        main = os.path.join(d, "SKILL.md")
        if not os.path.isdir(d) or (only and name not in only):
            continue
        if not os.path.isfile(main):
            problems.append(f"{name}: no SKILL.md")
            continue
        text = open(main, encoding="utf-8").read()
        fm = frontmatter(text)
        if fm is None:
            problems.append(f"{name}: missing frontmatter")
        else:
            if fm.get("name") != name:
                problems.append(f"{name}: frontmatter name {fm.get('name')!r} != directory")
            if not fm.get("description"):
                problems.append(f"{name}: empty description")
            elif len(fm["description"]) > DESCRIPTION_MAX:
                problems.append(f"{name}: description over {DESCRIPTION_MAX} characters")
            explicit = fm.get("disable-model-invocation") == "true"
            policy = os.path.join(d, POLICY)
            hidden = os.path.isfile(policy) and re.search(
                r"^policy:\s*\n(?:[ \t]+.*\n)*?[ \t]+allow_implicit_invocation:\s*false\b",
                open(policy, encoding="utf-8").read(), re.M)
            if explicit and not hidden:
                problems.append(f"{name}: explicit-only skill needs {POLICY} with allow_implicit_invocation: false")
            elif hidden and not explicit:
                problems.append(f"{name}: hidden from implicit use but not disable-model-invocation")
        limit = CORE_MAX if name in CORE else OTHER_MAX
        if len(text.encode()) > limit:
            problems.append(f"{name}: SKILL.md {len(text.encode())} bytes > {limit}")
        for dirpath, _, files in os.walk(d):
            for f in files:
                if not f.endswith(".md"):
                    continue
                p = os.path.join(dirpath, f)
                body = open(p, encoding="utf-8").read()
                rel = os.path.relpath(p, root)
                for pat, why in FORBIDDEN:
                    for m in re.finditer(pat, body, re.I):
                        line = body.count("\n", 0, m.start()) + 1
                        problems.append(f"{rel}:{line}: {why}: {m.group(0)[:40]!r}")
                for m in re.finditer(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", body):
                    t = m.group(1)
                    if re.match(r"(https?:|mailto:)", t):
                        continue
                    if not os.path.exists(os.path.normpath(os.path.join(dirpath, t))):
                        problems.append(f"{rel}: broken link {t}")
    return problems


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--only=")]
    only = next((a[7:].split(",") for a in sys.argv[1:] if a.startswith("--only=")), None)
    root = args[0] if args else os.path.join(os.path.dirname(__file__), "..")
    probs = check(root, only)
    for p in probs:
        print(p)
    print(f"{len(probs)} problem(s)")
    sys.exit(1 if probs else 0)
