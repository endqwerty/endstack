import os, tempfile, unittest, importlib.util

spec = importlib.util.spec_from_file_location("cs", os.path.join(os.path.dirname(__file__), "check-skills.py"))
cs = importlib.util.module_from_spec(spec); spec.loader.exec_module(cs)


def tree(files):
    d = tempfile.mkdtemp()
    for path, text in files.items():
        p = os.path.join(d, path); os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, "w", newline="").write(text)   # keep line endings exactly as given
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

    def test_explicit_skills_are_hidden_from_both_catalogs(self):
        hidden = GOOD.replace("description: Does x. Use for x.", "description: Does x.\ndisable-model-invocation: true")
        policy = "policy:\n  allow_implicit_invocation: false\n"
        self.assertTrue(any("agents/openai.yaml" in s for s in cs.check(tree({"skills/x/SKILL.md": hidden}))))
        self.assertEqual(cs.check(tree({"skills/x/SKILL.md": hidden, "skills/x/agents/openai.yaml": policy})), [])
        p = cs.check(tree({"skills/x/SKILL.md": GOOD, "skills/x/agents/openai.yaml": policy}))
        self.assertTrue(any("but not disable-model-invocation" in s for s in p))
        # Anything but the exact canonical file is rejected, so no YAML reading can disagree with it.
        for bad in ("allow_implicit_invocation: false\n",
                    "policy:\n  allow_implicit_invocation: true\n  unrelated:\n    allow_implicit_invocation: false\n",
                    "policy:\n  allow_implicit_invocation: false\npolicy:\n  allow_implicit_invocation: true\n",
                    'policy:\n  allow_implicit_invocation: "false"\n',
                    "policy:\n\tallow_implicit_invocation: false\n",
                    "policy:\n  allow_implicit_invocation: false junk\n",
                    "interface:\n  display_name: \"X\"\npolicy:\n  allow_implicit_invocation: false\n",
                    "policy:\r\n  allow_implicit_invocation: false\r\n",
                    "policy:\r  allow_implicit_invocation: false\r"):
            p = cs.check(tree({"skills/x/SKILL.md": hidden, "skills/x/agents/openai.yaml": bad}))
            self.assertTrue(any("agents/openai.yaml" in s for s in p), bad)

    def test_description_budget(self):
        long = GOOD.replace("Does x. Use for x.", "Does x. " * 30)
        self.assertTrue(any("description over 200" in s for s in cs.check(tree({"skills/x/SKILL.md": long}))))


if __name__ == "__main__":
    unittest.main()
