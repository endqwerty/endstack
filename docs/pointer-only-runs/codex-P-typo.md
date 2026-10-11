# Codex run P-typo (pointer v4, task typo)

Codex CLI headless, isolated CODEX_HOME with the global text and the six skills. Events in order:

```
MSG I’ll fix the README typo, check the diff, and commit it on a branch before fast-forwarding it into `main`.
1 ['SKILL-READ'] 'cat /tmp/scratch/codexP/skills/build/SKILL.md'
2 [] "pwd && git status --short --branch && git branch --show-current && rg --files -g 'AGENTS.md' -g 'README*' -g '*test*'"
MSG I’m using the build skill for this fix. The project’s local-only delivery rule calls for a fast-forward into `main`.
3 ['SKILL-READ'] 'cat /tmp/scratch/codexP/skills/verify/SKILL.md'
4 [] "cat AGENTS.md README.md test_shop.py && git log -3 --oneline && rg -n 'shpi|ship' ."
5 [] 'git switch -c fix/readme-shipping-typo'
FILECHANGE ['/tmp/scratch/run-XP-typo/README.md']
6 ['TESTS'] 'PYTHONDONTWRITEBYTECODE=1 python3 -m unittest && git diff --check && git diff -- README.md && git status --short'
7 ['MERGE'] "git add README.md && git commit -m 'docs: fix shipping typo in README' && git switch main && git merge --ff-only fix/readme-shipping-typo && git branch -d fix/readme-shipping-typo && git status --sho
MSG Fixed `shpi` → `ship` in README and fast-forwarded commit `ccceb68` into local `main`.  Both tests pass; working tree is clean.
```

Final git state:

```
main: ccceb68 docs: fix shipping typo in README
```
