import os, tempfile, unittest, importlib.util

spec = importlib.util.spec_from_file_location("cr", os.path.join(os.path.dirname(__file__), "check-routing.py"))
cr = importlib.util.module_from_spec(spec); spec.loader.exec_module(cr)


def tree(routing, skills=("a", "b", "c")):
    d = tempfile.mkdtemp()
    for s in skills:
        os.makedirs(os.path.join(d, "skills", s))
    if routing is not None:
        open(os.path.join(d, "ROUTING.md"), "w").write(routing)
    return d


GOOD = "Skip casual chat.\n- prose: `unslop`, docs `technical-writing`\n- merge: `ship`, `autopilot-full` only when explicitly asked\n\nOnly when named: `c`\n"
SK = ("unslop", "technical-writing", "c", "ship", "autopilot-full")


class T(unittest.TestCase):
    def test_good(self):
        self.assertEqual(cr.check(tree(GOOD, SK)), [])

    def test_missing_file(self):
        self.assertEqual(cr.check(tree(None)), ["ROUTING.md: missing"])

    def test_unrouted_and_unknown_skills(self):
        p = " ".join(cr.check(tree(GOOD + "`ghost`\n", SK + ("orphan",))))
        self.assertIn("`ghost` is not a skill", p); self.assertIn("skill orphan is not routed", p)

    def test_external_skills_may_be_routed_but_not_twice(self):
        self.assertEqual(cr.check(tree(GOOD + "- states: `statechart`, pictures `archify`\n", SK)), [])
        self.assertIn("skill archify appears 2 times",
                      " ".join(cr.check(tree(GOOD + "`archify` `archify`\n", SK))))

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

    def test_casual_skip_required(self):
        self.assertIn("casual chat", " ".join(cr.check(tree(GOOD.replace("casual", "quiet"), SK))))

    def test_size_and_forbidden_terms(self):
        p = " ".join(cr.check(tree(GOOD + "word " * 700 + "Use Claude, run `git push`.\n", SK)))
        self.assertIn("bytes >", p); self.assertIn("model or provider name", p); self.assertIn("command in backticks", p)


if __name__ == "__main__":
    unittest.main()
