import os, tempfile, unittest, importlib.util

spec = importlib.util.spec_from_file_location("cs", os.path.join(os.path.dirname(__file__), "check-skills.py"))
cs = importlib.util.module_from_spec(spec); spec.loader.exec_module(cs)


def tree(files):
    d = tempfile.mkdtemp()
    for path, text in files.items():
        p = os.path.join(d, path); os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, "w").write(text)
    return d


GOOD = "---\nname: x\ndescription: Does x. Use for x.\n---\n\n# X\n\nDo it.\n"


class T(unittest.TestCase):
    def test_good(self):
        self.assertEqual(cs.check(tree({"skills/x/SKILL.md": GOOD})), [])

    def test_name_mismatch_and_missing_description(self):
        p = cs.check(tree({"skills/x/SKILL.md": "---\nname: y\ndescription:\n---\nbody\n"}))
        self.assertTrue(any("!= directory" in s for s in p) and any("empty description" in s for s in p))

    def test_forbidden_terms(self):
        body = GOOD + "Run `git push`. Ask the Task tool. Use Claude or gpt-6. /loop in Cursor.\n"
        p = " ".join(cs.check(tree({"skills/x/SKILL.md": body})))
        for w in ("command in backticks", "harness tool name", "model or provider name", "harness slash command", "harness name"):
            self.assertIn(w, p)

    def test_references_and_links_are_checked(self):
        t = tree({"skills/x/SKILL.md": GOOD + "[r](references/a.md)\n", "skills/x/references/a.md": "see Opus [gone](nope.md)\n"})
        p = " ".join(cs.check(t))
        self.assertIn("model or provider name", p); self.assertIn("broken link nope.md", p)

    def test_size_limits(self):
        self.assertEqual(cs.check(tree({"skills/x/SKILL.md": GOOD + "word " * 1000})), [])
        core = GOOD.replace("name: x", "name: build") + "word " * 600
        self.assertTrue(any("bytes" in s for s in cs.check(tree({"skills/build/SKILL.md": core}))))


if __name__ == "__main__":
    unittest.main()
