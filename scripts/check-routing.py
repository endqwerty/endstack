#!/usr/bin/env python3
"""Lint ROUTING.md: size, portability, and that every installable skill is routed
exactly where it belongs. Exit 1 on any problem."""
import importlib.util, json, os, re, sys

spec = importlib.util.spec_from_file_location("cs", os.path.join(os.path.dirname(os.path.abspath(__file__)), "check-skills.py"))
cs = importlib.util.module_from_spec(spec); spec.loader.exec_module(cs)

MAX = 2800  # bytes: read on every turn, so it stays small
NAMED = "Only when named:"
EXTERNAL = {"archify", "statechart"}  # installed by homelab from other pinned sources, not skills/
PLUGIN_KEYS = {"name", "repository", "revision", "marketplace", "skills"}
SKILL_NAME = r"[a-z][a-z0-9-]*"


def plugin_skills(root, local):
    """Skill names the plugins in plugins.json install, and the problems in that file."""
    path = os.path.join(root, "plugins.json")
    if not os.path.isfile(path):
        return set(), []
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except ValueError as e:
        return set(), [f"plugins.json: not valid JSON ({e}); fix the syntax"]
    if not isinstance(data, dict) or set(data) != {"plugins"} or not isinstance(data["plugins"], list):
        return set(), ['plugins.json: expected {"plugins": [...]} and nothing else; restore that shape']
    names, problems, seen = set(), [], set()
    for i, p in enumerate(data["plugins"]):
        where = f"plugins.json: plugin {i}"
        if not isinstance(p, dict) or set(p) != PLUGIN_KEYS:
            got = sorted(p) if isinstance(p, dict) else type(p).__name__
            problems.append(f"{where}: keys {got} != {sorted(PLUGIN_KEYS)}; give it exactly those keys")
            continue
        where = f"plugins.json: plugin {p['name']!r}"
        for k in ("name", "marketplace"):
            if not isinstance(p[k], str) or not re.fullmatch(SKILL_NAME, p[k]):
                problems.append(f"{where}: {k} must be a lowercase name; use letters, digits and hyphens")
        if isinstance(p["name"], str):
            if p["name"] in seen:
                problems.append(f"{where}: listed twice; merge the entries")
            seen.add(p["name"])
        if not isinstance(p["repository"], str) or not re.fullmatch(r"https://\S+", p["repository"]):
            problems.append(f"{where}: repository must be an https URL; give the clone URL")
        if not isinstance(p["revision"], str) or not re.fullmatch(r"[0-9a-f]{40}", p["revision"]):
            problems.append(f"{where}: revision must be a full 40-character commit hash; pin the exact commit, not a branch or tag")
        skills = p["skills"]
        if not isinstance(skills, list) or not skills or not all(isinstance(s, str) and re.fullmatch(SKILL_NAME, s) for s in skills):
            problems.append(f"{where}: skills must be a non-empty list of skill names; list the plugin's skill directory names")
            continue
        for s in sorted(set(skills)):
            if skills.count(s) > 1 or s in names:
                problems.append(f"plugins.json: skill {s} listed more than once; keep one entry")
            if s in local:
                problems.append(f"plugins.json: skill {s} also exists in skills/; delete one of the two")
            if s in EXTERNAL:
                problems.append(f"plugins.json: skill {s} is also in EXTERNAL; drop it from EXTERNAL")
        names |= set(skills)
    return names, problems


def check(root):
    path = os.path.join(root, "ROUTING.md")
    if not os.path.isfile(path):
        return ["ROUTING.md: missing; restore it from the default branch"]
    with open(path, encoding="utf-8") as f:
        text = f.read()
    problems = []
    if len(text.encode()) > MAX:
        problems.append(f"ROUTING.md: {len(text.encode())} bytes > {MAX}; shorten a bullet, every turn pays for this file")
    for pat, why, fix in cs.FORBIDDEN:
        for m in re.finditer(pat, text, re.I):
            problems.append(f"ROUTING.md:{text.count(chr(10), 0, m.start()) + 1}: {why}: {m.group(0)[:40]!r}; {fix}")
    skills = {d for d in os.listdir(os.path.join(root, "skills")) if os.path.isdir(os.path.join(root, "skills", d))}
    plugins, plugin_problems = plugin_skills(root, skills)
    problems += plugin_problems
    external = EXTERNAL | plugins
    names = re.findall(r"`([a-z][a-z0-9-]*)`", text)
    for name in sorted(set(names) - skills - external):
        problems.append(f"ROUTING.md: `{name}` is not a skill in skills/ or plugins.json; fix the name, or list it under its plugin in plugins.json")
    for name in sorted(external & set(names)):
        if names.count(name) > 1:
            problems.append(f"ROUTING.md: skill {name} appears {names.count(name)} times, expected once; keep one mention and delete the others")
    for name in sorted(skills):
        n = names.count(name)
        if n == 0:
            problems.append(f"ROUTING.md: skill {name} is not routed; add it to the bullet for its task, or to the '{NAMED}' line")
        elif n > 1:
            problems.append(f"ROUTING.md: skill {name} appears {n} times, expected once; keep one mention and delete the others")
    at = text.find(NAMED)
    if at < 0:
        problems.append(f"ROUTING.md: no '{NAMED}' line; add it as the last paragraph")
    elif not re.findall(r"`([a-z][a-z0-9-]*)`", re.split(r"\n\s*\n", text[at:], maxsplit=1)[0]):
        problems.append(f"ROUTING.md: '{NAMED}' lists no skill; list the skills loaded only by name there")
    bullets = [b for b in re.split(r"\n(?=- )", text[:at] if at >= 0 else text) if b.startswith("- ")]

    def bullet_with(name):
        return next((b for b in bullets if f"`{name}`" in b), "")

    prose = bullet_with("unslop")
    if "`technical-writing`" not in prose or "docs" not in prose.lower():
        problems.append("ROUTING.md: one bullet must route prose to unslop and docs to technical-writing; name both in one bullet that also says docs")
    for name in ("ship", "autopilot-full"):
        if "explicit" not in bullet_with(name):
            problems.append(f"ROUTING.md: `{name}` must be routed only on an explicit request; say 'explicit' in its bullet")
    named = re.split(r"\n\s*\n", text[at:], maxsplit=1)[0] if at >= 0 else ""
    if "`orchestrate`" in text and "`orchestrate`" not in named and "explicit" not in bullet_with("orchestrate"):
        problems.append("ROUTING.md: `orchestrate` may land only on an explicit request; say so with 'explicit' in its bullet, or list it under '" + NAMED + "'")
    if "casual" not in text.lower():
        problems.append("ROUTING.md: must say casual chat skips routing; add it to the opening paragraph")
    return problems


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    probs = check(root)
    for p in probs:
        print(p)
    print(f"{len(probs)} problem(s)")
    sys.exit(1 if probs else 0)
