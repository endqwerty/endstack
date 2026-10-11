# Run D-typo (arm D, task typo)

Tool-call order (selected events):

```
   (2, "EDIT/COMMIT: git checkout -q -b fix-readme-typo && sed -i '4s/shpi/ship/' README.md && git diff --stat ")
   (2, 'RUN TESTS')
```

Final git state:

```
main: 71a57dd Fix typo in README: shpi -> ship
branches: main 
```

Final report:

I fixed the typo in `README.md` line 4 ("shpi" is now "ship"). It's fast-forwarded onto `main` as commit `71a57dd`, "Fix typo in README: shpi -> ship".

The unit tests pass (2 tests). I made the change on a branch, merged it into `main`, and deleted the branch. I didn't use the `verify` skill, since this is a one-word docs edit that changes no behavior.
