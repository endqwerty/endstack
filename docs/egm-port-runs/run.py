"""Paired dry run: old vs new goldfish, interview and drift text. Usage: python3 run.py <endstack worktree> <out dir>."""
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2])
BASE = "origin/main"
FILES = [
    ("ROUTING", "ROUTING.md"),
    ("BUILD DESIGN REFERENCE", "skills/build/references/design.md"),
    ("INTERVIEW SKILL", "skills/interview/SKILL.md"),
    ("GOLDFISH SKILL", "skills/goldfish/SKILL.md"),
    ("GOLDFISH BRIEF", "skills/goldfish/references/goldfish-prompt.md"),
    ("GOLDFISH REVIEWER ROLES", "skills/goldfish/references/reviewers.md"),
    ("GOLDFISH STANDARDS", "skills/goldfish/references/standards.md"),
    ("DRIFT SKILL", "skills/drift/SKILL.md"),
]
HEADER = (
    "This is a tool-free policy simulation. Do not use tools, read files, or perform any real "
    "action. Apply only the supplied skill context to the scenario. State exactly what you do "
    "next and why, in at most 10 lines, in order. Describe intended actions, not completed actions."
)
SCENARIOS = json.loads((Path(__file__).parent / "inputs.json").read_text())["scenarios"]


def text(arm, path):
    if arm == "old":
        r = subprocess.run(["git", "-C", str(ROOT), "show", f"{BASE}:{path}"],
                           capture_output=True, text=True)
        return r.stdout if r.returncode == 0 else None
    return (ROOT / path).read_text()


def prompt(arm, scenario):
    parts = [HEADER, ""]
    for label, path in FILES:
        t = text(arm, path)
        if t is not None:
            parts += [f"{label}:", t, ""]
    parts += ["SCENARIO:", scenario]
    return "\n".join(parts)


def run(job):
    n, arm, scenario = job
    stem = OUT / f"{n}-{arm}"
    p = prompt(arm, scenario)
    Path(f"{stem}-prompt.txt").write_text(p)
    with open(f"{stem}-events.jsonl", "w") as ev:
        rc = subprocess.run(
            ["codex", "exec", "--ignore-user-config", "--ignore-rules", "--ephemeral",
             "--skip-git-repo-check", "-s", "read-only", "--json",
             "-o", f"{stem}-answer.txt", "-"],
            input=p, text=True, stdout=ev, stderr=subprocess.STDOUT, cwd="/tmp").returncode
    Path(f"{stem}-rc.txt").write_text(f"{rc}\n")
    return n, arm, rc


OUT.mkdir(parents=True, exist_ok=True)
jobs = [(i + 1, arm, s) for i, s in enumerate(SCENARIOS) for arm in ("old", "new")]
with ThreadPoolExecutor(max_workers=7) as pool:
    for n, arm, rc in pool.map(run, jobs):
        print(n, arm, "rc", rc, flush=True)
