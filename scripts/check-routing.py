#!/usr/bin/env python3
"""Lint ROUTING.md: size, portability, and that every installable skill is routed
exactly where it belongs. Exit 1 on any problem."""
import importlib.util, json, os, re, sys

spec = importlib.util.spec_from_file_location("cs", os.path.join(os.path.dirname(os.path.abspath(__file__)), "check-skills.py"))
cs = importlib.util.module_from_spec(spec); spec.loader.exec_module(cs)

MAX = None  # bytes; off until the next trim pass sets it again
NAMED = "Only when named:"
EXTERNAL = {"archify", "statechart"}  # installed by homelab from other pinned sources, not skills/
PLUGIN_KEYS = {"name", "repository", "revision", "marketplace", "skills"}
SOURCE = "endstack"  # homelab's name for this skill source; a plugin may not reuse it


def safe_name(value):
    """homelab's safe_name: the names its sync accepts for plugins, marketplaces and skills."""
    return (isinstance(value, str) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", value) is not None
            and value.casefold() not in {"synced", "backup"})


def plugin_skills(root, local):
    """Skill names the plugins in plugins.json install, and the problems in that file.

    Mirrors read_manifest in homelab's homelab_cli/plugins.py, which rejects the whole file
    on any of these, plus endstack's own rule that a plugin skill is not also in skills/."""
    path = os.path.join(root, "plugins.json")
    if os.path.islink(path):
        return set(), ["plugins.json: is a symlink, which homelab sync rejects; replace it with the file itself"]
    if not os.path.exists(path):
        return set(), []
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError) as e:
        return set(), [f"plugins.json: not valid JSON ({e}); fix the syntax"]
    if not isinstance(data, dict) or set(data) != {"plugins"} or not isinstance(data["plugins"], list):
        return set(), ['plugins.json: expected {"plugins": [...]} and nothing else; restore that shape']
    names, problems, seen, markets = set(), [], {SOURCE}, set()
    folded_local = {s.casefold() for s in local}
    for i, p in enumerate(data["plugins"]):
        if not isinstance(p, dict) or set(p) != PLUGIN_KEYS:
            got = sorted(p) if isinstance(p, dict) else type(p).__name__
            problems.append(f"plugins.json: plugin {i}: keys {got} != {sorted(PLUGIN_KEYS)}; give it exactly those keys")
            continue
        name, market, repo, rev, skills = (p[k] for k in ("name", "marketplace", "repository", "revision", "skills"))
        where = f"plugins.json: plugin {name!r}"
        if not safe_name(name):
            problems.append(f"{where}: name must be a safe name (letters, digits, '_' or '-', not synced or backup); rename it")
        elif name.casefold() in seen:
            problems.append(f"{where}: name is used twice or is the source's own name ({SOURCE}); give it a distinct name")
        else:
            seen.add(name.casefold())
        if not safe_name(market):
            problems.append(f"{where}: marketplace must be a safe name (letters, digits, '_' or '-', not synced or backup); rename it")
        elif market.casefold() in markets:
            problems.append(f"{where}: marketplace {market!r} is shared with another plugin; give each plugin its own marketplace")
        else:
            markets.add(market.casefold())
        if (not isinstance(repo, str) or not repo.strip() or "\x00" in repo or repo.startswith("-")
                or not (":" in repo or os.path.isabs(repo))):
            problems.append(f"{where}: repository must be a URL or an absolute path; give the clone URL")
        if not isinstance(rev, str) or not re.fullmatch(r"[0-9a-fA-F]{40}", rev):
            problems.append(f"{where}: revision must be a full 40-character commit hash; pin the exact commit, not a branch or tag")
        if (not isinstance(skills, list) or not all(safe_name(s) for s in skills)
                or len({s.casefold() for s in skills}) != len(skills)):
            problems.append(f"{where}: skills must be a list of distinct safe names; list the plugin's skill directory names once each")
            continue
        for s in skills:
            if s.casefold() in {n.casefold() for n in names}:
                problems.append(f"plugins.json: skill {s} is listed by two plugins; keep it under one")
            if s.casefold() in folded_local:
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
    if MAX is not None and len(text.encode()) > MAX:
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
