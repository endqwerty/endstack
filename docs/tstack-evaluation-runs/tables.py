"""Recompute the round tables in docs/tstack-evaluation.md.

Unit: a verify round is one distinct (repository, pull request, round
number); two records with the same number are merged. A "later round" is
round 2 or more. Usage: python3 -I tables.py mainworthy.jsonl others.jsonl
"""
import collections
import json
import sys

rounds = {}
for path in sys.argv[1:]:
    for line in open(path):
        r = json.loads(line)
        if r["kind"] != "verify":
            continue
        key = (r["repo"], r["pr"], r["round"])
        found = [f for f in r["findings"] if not f.get("preexisting_on_main")]
        if key in rounds:
            rounds[key]["findings"] += found
            if r["verdict"] == "issues":
                rounds[key]["verdict"] = "issues"
        else:
            rounds[key] = {"verdict": r["verdict"], "findings": found}

table = collections.Counter()
count = collections.Counter()
for (repo, pr, n), r in rounds.items():
    band = min(n, 4)
    count[band] += 1
    for f in r["findings"]:
        table[(band, f["class"])] += 1
print("round  rounds  bug  risk  nit  false_positive")
for band in (1, 2, 3, 4):
    print(band, count[band], *(table[(band, c)] for c in ("bug", "risk", "nit", "false_positive")))

prs = collections.defaultdict(dict)
for (repo, pr, n), r in rounds.items():
    prs[(repo, pr)][n] = r
starts = collections.Counter()
bugs = collections.Counter()
for rs in prs.values():
    order = sorted(rs)
    for prev, cur in zip(order, order[1:]):
        p, c = rs[prev], rs[cur]
        classes = {f["class"] for f in p["findings"]}
        has_bug = any(f["class"] == "bug" for f in c["findings"])
        kinds = []
        if p["verdict"] == "pass":
            kinds.append("after a pass")
        elif classes and classes <= {"nit", "false_positive"}:
            kinds.append("after a non-pass with only nits")
        if p["verdict"] != "pass" and classes and classes <= {"nit", "false_positive", "risk"}:
            kinds.append("after a non-pass with only nits or risks")
        if cur > 3:
            kinds.append("beyond round 3")
        kinds.append("all later rounds")
        for k in kinds:
            starts[k] += 1
            bugs[k] += has_bug
for k in sorted(starts):
    print(f"{k}: {starts[k]} rounds, {bugs[k]} with a bug")
