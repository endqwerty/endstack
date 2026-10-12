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


GOOD = "Skip on a casual turn.\n- prose: `unslop`, docs `technical-writing`\nOnly when named: `c`\n"
SK = ("unslop", "technical-writing", "c")


class T(unittest.TestCase):
    def test_good(self):
        self.assertEqual(cr.check(tree(GOOD, SK)), [])

    def test_missing_file(self):
        self.assertEqual(cr.check(tree(None)), ["ROUTING.md: missing"])

    def test_unrouted_and_unknown_skills(self):
        p = " ".join(cr.check(tree(GOOD + "`ghost`\n", SK + ("orphan",))))
        self.assertIn("`ghost` is not a skill", p); self.assertIn("skill orphan is not routed", p)

    def test_named_and_routed_conflict(self):
        p = " ".join(cr.check(tree(GOOD + "- `c` for x\n", SK)))
        self.assertIn("both routed and 'only when named'", p)

    def test_required_routes_and_named_line(self):
        p = " ".join(cr.check(tree("Only when named: `x`\n", ("x",))))
        for w in ("route to unslop", "route to technical-writing", "casual turn"):
            self.assertIn(w, p)
        self.assertIn("no 'Only when named:' line", " ".join(cr.check(tree("casual unslop technical-writing `unslop` `technical-writing`\n", ("unslop", "technical-writing")))))

    def test_size_and_forbidden_terms(self):
        p = " ".join(cr.check(tree(GOOD + "word " * 700 + "Use Claude, run `git push`.\n", SK)))
        self.assertIn("bytes >", p); self.assertIn("model or provider name", p); self.assertIn("command in backticks", p)


if __name__ == "__main__":
    unittest.main()
