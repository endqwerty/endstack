# Run F-typo (arm F, task typo)

Tool-call order (selected events):

```
   (2, "EDIT/COMMIT: git checkout -q -b fix-readme-typo && sed -i '4s/shpi/ship/' README.md && git diff --stat ")
   (2, 'RUN TESTS')
   (2, 'MERGE')
```

Final git state:

```
main: d6724c4 Fix typo in README: shpi -> ship
branches: main 
```

Final report:

I fixed the typo in `README.md` line 4 ("shpi" is now "ship"). It is fast-forward merged into `main` as `d6724c4`.

I worked on a branch and then deleted it after the merge. The 2 tests pass, but they don't cover the README. Since this was a docs-only change, I skipped the independent `verify` step.
