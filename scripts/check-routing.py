#!/usr/bin/env python3
"""Lint ROUTING.md: size, portability, and that every installable skill is routed
exactly where it belongs. Exit 1 on any problem."""
import importlib.util, os, re, sys

spec = importlib.util.spec_from_file_location("cs", os.path.join(os.path.dirname(os.path.abspath(__file__)), "check-skills.py"))
cs = importlib.util.module_from_spec(spec); spec.loader.exec_module(cs)

MAX = 2600  # bytes: read on every turn, so it stays small
NAMED = "Only when named:"


def check(root):
    path = os.path.join(root, "ROUTING.md")
    if not os.path.isfile(path):
        return ["ROUTING.md: missing"]
    text = open(path, encoding="utf-8").read()
    problems = []
    if len(text.encode()) > MAX:
        problems.append(f"ROUTING.md: {len(text.encode())} bytes > {MAX}")
    for pat, why in cs.FORBIDDEN:
        for m in re.finditer(pat, text, re.I):
            problems.append(f"ROUTING.md:{text.count(chr(10), 0, m.start()) + 1}: {why}: {m.group(0)[:40]!r}")
    skills = {d for d in os.listdir(os.path.join(root, "skills")) if os.path.isdir(os.path.join(root, "skills", d))}
    names = re.findall(r"`([a-z][a-z0-9-]*)`", text)
    for name in sorted(set(names) - skills):
        problems.append(f"ROUTING.md: `{name}` is not a skill in skills/")
    for name in sorted(skills):
        n = names.count(name)
        if n == 0:
            problems.append(f"ROUTING.md: skill {name} is not routed")
        elif n > 1:
            problems.append(f"ROUTING.md: skill {name} appears {n} times, expected once")
    at = text.find(NAMED)
    if at < 0:
        problems.append(f"ROUTING.md: no '{NAMED}' line")
    elif not re.findall(r"`([a-z][a-z0-9-]*)`", text[at:]):
        problems.append(f"ROUTING.md: '{NAMED}' lists no skill")
    bullets = [b for b in re.split(r"\n(?=- )", text[:at] if at >= 0 else text) if b.startswith("- ")]

    def bullet_with(name):
        return next((b for b in bullets if f"`{name}`" in b), "")

    prose = bullet_with("unslop")
    if "`technical-writing`" not in prose or "docs" not in prose.lower():
        problems.append("ROUTING.md: one bullet must route prose to unslop and docs to technical-writing")
    for name in ("ship", "autopilot-full"):
        if "explicit" not in bullet_with(name):
            problems.append(f"ROUTING.md: `{name}` must be routed only on an explicit request")
    if "casual" not in text.lower():
        problems.append("ROUTING.md: must say casual chat skips routing")
    return problems


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    probs = check(root)
    for p in probs:
        print(p)
    print(f"{len(probs)} problem(s)")
    sys.exit(1 if probs else 0)
