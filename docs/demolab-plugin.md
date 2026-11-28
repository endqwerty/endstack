# Gemini DemoLab plugin

## Why (2026-11-28)

Daniel asked whether Google's [Gemini DemoLab](https://github.com/google-gemini/demolab)
skills belong in his stack, then asked for the frontend skill as a pinned plugin
on every provider. DemoLab at `6a5e364` has two skills:

- `gemini-frontend-design` (16 KB): design rules for web pages and apps
  (palette beyond beige, no eyebrow labels or decorative chips, no 50/50 hero,
  at most three body font sizes, reduced motion, a rendered check at desktop
  and phone width). Too large for a role skill in `skills/` (6,000 bytes) and it
  names an image tool, so it is pinned, not ported, like EGM.
- `deep-research`: not routed. The harnesses already ship research
  orchestration, and `swarm` covers fan-out. A plugin installs whole, so it
  still arrives, and neither DemoLab skill is hidden: both stay in every
  harness's catalog and can load on their own (a probe listed
  `demolab:deep-research` in Claude Code). Accepted: one description line per
  request. Hiding it needs a fork or a homelab override, not worth it for one
  line; revisit if it starts loading on research questions.

## Change

- `plugins.json` pins `demolab@demolab` at `6a5e364`; homelab sync installs
  it into Claude Code, Codex and Antigravity.
- `ROUTING.md` routes building or restyling a web page or web app UI to
  `gemini-frontend-design`, and its read rule now says "a plugin skill: its
  plugin's" instead of naming EGM. The cap rises from 3,000 to 3,100 bytes
  for the new route; the existing routes keep their tested wording.
- `check-routing.py` skips the provider-name scan inside a backticked name that
  `plugins.json` declares, since the plugin fixes the skill's name;
  `check-evals.py` accepts plugin skills as case tags.

## Eval

`frontend-landing`, one run per arm, `main` against `695ee2f`:

| Agent | main | head | What changed |
|---|---|---|---|
| Claude | 0.88 | 1.00 | read the skill; main already met every output check |
| Codex | 0.75 | 1.00 | read the skill; main used eyebrow labels, head did not |
| Antigravity | not run | not run | `agy -p` asked for a browser sign-in and timed out |

The output checks (reduced motion, no `transition: all`, eyebrow labels, em
dashes, numbered headings or remote images) barely separate the arms, so this
shows the route and load work, not that pages got better. A visual judgment of
the rendered pages would need a screenshot grader that the runner lacks.
DemoLab's own 67% and 75% preference figures were measured on Gemini models.

To reverse: delete the `demolab` entry from `plugins.json` and the route line,
then move homelab's endstack pin; sync uninstalls the plugin.
