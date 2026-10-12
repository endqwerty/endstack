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
    named_line = next((l for l in text.splitlines() if l.startswith(NAMED)), None)
    if named_line is None:
        problems.append(f"ROUTING.md: no '{NAMED}' line")
    routed = set(re.findall(r"`([a-z][a-z0-9-]*)`", text))
    for name in sorted(routed - skills):
        problems.append(f"ROUTING.md: `{name}` is not a skill in skills/")
    for name in sorted(skills - routed):
        problems.append(f"ROUTING.md: skill {name} is not routed")
    if named_line:
        for name in re.findall(r"`([a-z][a-z0-9-]*)`", named_line):
            if text.count(f"`{name}`") > 1:
                problems.append(f"ROUTING.md: `{name}` is both routed and 'only when named'")
    for needle, why in (("unslop", "prose must route to unslop"), ("technical-writing", "docs must route to technical-writing"),
                        ("casual", "must say a casual turn skips routing")):
        if needle not in text:
            problems.append(f"ROUTING.md: {why}")
    return problems


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    probs = check(root)
    for p in probs:
        print(p)
    print(f"{len(probs)} problem(s)")
    sys.exit(1 if probs else 0)
