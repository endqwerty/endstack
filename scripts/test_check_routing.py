import json, os, tempfile, unittest, importlib.util

spec = importlib.util.spec_from_file_location("cr", os.path.join(os.path.dirname(__file__), "check-routing.py"))
cr = importlib.util.module_from_spec(spec); spec.loader.exec_module(cr)


def tree(routing, skills=("a", "b", "c"), plugins=None):
    d = tempfile.mkdtemp()
    for s in skills:
        os.makedirs(os.path.join(d, "skills", s))
    if routing is not None:
        open(os.path.join(d, "ROUTING.md"), "w").write(routing)
    if plugins is not None:
        open(os.path.join(d, "plugins.json"), "w").write(plugins if isinstance(plugins, str) else json.dumps(plugins))
    return d


def plugin(**over):
    p = {"name": "egm", "repository": "https://example.com/egm.git", "revision": "8b1553f5c6dc84c60b7e065f0040199d72c54c54",
         "marketplace": "egm", "skills": ["egm-review", "egm-lite"]}
    p.update(over)
    return {"plugins": [p]}


GOOD = "Skip casual chat.\n- prose: `unslop`, docs `technical-writing`\n- merge: `ship`, `autopilot-full` only when explicitly asked\n\nOnly when named: `c`\n"
SK = ("unslop", "technical-writing", "c", "ship", "autopilot-full")


class T(unittest.TestCase):
    def test_good(self):
        self.assertEqual(cr.check(tree(GOOD, SK)), [])

    def test_missing_file(self):
        self.assertEqual(cr.check(tree(None)), ["ROUTING.md: missing; restore it from the default branch"])

    def test_every_problem_names_its_fix(self):
        bad = "- `ghost` `a` `a` with Claude via `git push`\n" + "x" * 2900
        p = cr.check(tree(bad, ("a", "b", "ship", "autopilot-full", "unslop")))
        p += cr.check(tree(GOOD.replace("`c`", "").replace("\n\nOnly", "\n- `archify` `archify`\n\nOnly"), SK))
        self.assertGreater(len(p), 8)
        for s in p:
            self.assertRegex(s, r"; \S", s)
        for kind in ("archify appears 2 times", "lists no skill"):
            self.assertTrue(any(kind in s for s in p), kind)

    def test_unrouted_and_unknown_skills(self):
        p = " ".join(cr.check(tree(GOOD + "`ghost`\n", SK + ("orphan",))))
        self.assertIn("`ghost` is not a skill", p); self.assertIn("skill orphan is not routed", p)

    def test_external_skills_may_be_routed_but_not_twice(self):
        self.assertEqual(cr.check(tree(GOOD + "- states: `statechart`, pictures `archify`\n", SK)), [])
        self.assertIn("skill archify appears 2 times",
                      " ".join(cr.check(tree(GOOD + "`archify` `archify`\n", SK))))

    def test_plugin_skills_may_be_routed_once_and_need_not_be(self):
        self.assertEqual(cr.check(tree(GOOD + "- review: `egm-review`\n", SK, plugin())), [])
        self.assertEqual(cr.check(tree(GOOD, SK, plugin())), [])
        self.assertIn("skill egm-review appears 2 times",
                      " ".join(cr.check(tree(GOOD + "`egm-review` `egm-review`\n", SK, plugin()))))

    def test_plugin_skill_unknown_without_plugins_json(self):
        p = " ".join(cr.check(tree(GOOD + "`egm-review`\n", SK)))
        self.assertIn("`egm-review` is not a skill in skills/ or plugins.json", p)

    def test_plugin_skill_must_not_also_be_local_or_external(self):
        p = " ".join(cr.check(tree(GOOD, SK + ("egm-review",), plugin())))
        self.assertIn("skill egm-review also exists in skills/", p)
        p = " ".join(cr.check(tree(GOOD, SK, plugin(skills=["archify"]))))
        self.assertIn("skill archify is also in EXTERNAL", p)

    def test_plugins_json_shape(self):
        bad = [
            ("{", "not valid JSON"),
            ([], "expected {\"plugins\": [...]}"),
            ({"plugins": [], "extra": 1}, "expected {\"plugins\": [...]}"),
            ({"plugins": [{"name": "egm"}]}, "give it exactly those keys"),
            (plugin(vendored=True), "give it exactly those keys"),
            (plugin(revision="main"), "full 40-character commit hash"),
            (plugin(revision="8b1553f"), "full 40-character commit hash"),
            (plugin(repository="git@github.com:google/egm.git"), "https URL"),
            (plugin(name="EGM"), "name must be a lowercase name"),
            (plugin(marketplace=3), "marketplace must be a lowercase name"),
            (plugin(skills=[]), "non-empty list"),
            (plugin(skills="egm-review"), "non-empty list"),
            (plugin(skills=["Egm Review"]), "non-empty list"),
            (plugin(skills=["egm-review", "egm-review"]), "listed more than once"),
            ({"plugins": plugin()["plugins"] * 2}, "listed twice"),
        ]
        for data, want in bad:
            p = cr.check(tree(GOOD, SK, data if isinstance(data, str) else json.dumps(data)))
            self.assertTrue(any(want in s for s in p), (data, want, p))
            for s in p:
                self.assertRegex(s, r"; \S", s)

    def test_repository_plugins_json_is_valid(self):
        root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
        names, problems = cr.plugin_skills(root, set())
        self.assertEqual(problems, [])
        self.assertIn("egm-review", names)

    def test_duplicate_route_and_named_conflict(self):
        self.assertIn("skill unslop appears 2 times", " ".join(cr.check(tree(GOOD.replace("docs", "`unslop` docs"), SK))))
        self.assertIn("skill c appears 2 times", " ".join(cr.check(tree(GOOD.replace("- merge", "- `c` merge"), SK))))

    def test_named_line_missing_or_empty(self):
        no_line = "\n".join(l for l in GOOD.splitlines() if not l.startswith("Only")).replace("`c`", "")
        self.assertIn("no 'Only when named:' line", " ".join(cr.check(tree(no_line, SK))))
        self.assertIn("lists no skill", " ".join(cr.check(tree(GOOD.replace("`c`", ""), SK))))
        later = GOOD.replace("`c`", "") + "\n- Always apply: `c`\n"
        self.assertIn("lists no skill", " ".join(cr.check(tree(later, SK))))

    def test_prose_and_docs_in_one_bullet(self):
        split = GOOD.replace("- prose: `unslop`, docs `technical-writing`", "- prose: `unslop`\n- docs: `technical-writing`")
        self.assertIn("one bullet must route prose", " ".join(cr.check(tree(split, SK))))

    def test_merge_skills_need_explicit_request(self):
        p = " ".join(cr.check(tree(GOOD.replace("only when explicitly asked", "to merge"), SK)))
        self.assertIn("`ship` must be routed only on an explicit request", p)
        self.assertIn("`autopilot-full` must be routed only on an explicit request", p)

    def test_routed_orchestrate_needs_explicit_landing(self):
        sk = SK + ("orchestrate",)
        routed = GOOD.replace("\n\nOnly", "\n- big change: `orchestrate` coordinates\n\nOnly")
        self.assertIn("`orchestrate` may land only on an explicit request", " ".join(cr.check(tree(routed, sk))))
        landing = routed.replace("coordinates", "coordinates, landing only on an explicit request")
        self.assertEqual(cr.check(tree(landing, sk)), [])
        outside = GOOD.replace("Skip casual chat.", "Skip casual chat. Use `orchestrate` for big changes.")
        self.assertIn("`orchestrate` may land only on an explicit request", " ".join(cr.check(tree(outside, sk))))
        named = GOOD.replace("`c`", "`c`, `orchestrate`")
        self.assertEqual(cr.check(tree(named, sk)), [])

    def test_casual_skip_required(self):
        self.assertIn("casual chat", " ".join(cr.check(tree(GOOD.replace("casual", "quiet"), SK))))

    def test_size_and_forbidden_terms(self):
        p = " ".join(cr.check(tree(GOOD + "word " * 700 + "Use Claude, run `git push`.\n", SK)))
        self.assertIn("bytes >", p); self.assertIn("model or provider name", p); self.assertIn("command in backticks", p)


if __name__ == "__main__":
    unittest.main()
