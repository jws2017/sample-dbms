import unittest
from tokenizer import tokenize

class TestLexer(unittest.TestCase):
    def test_table_creation(self):
        tokens = tokenize("CREATE TABLE thingy(col1 int, col2 string);")
        self.assertIsInstance(tokens, dict, "tokenize does not return dict")
        self.assertIn("action", tokens, "action key not set")
        self.assertEqual(tokens["action"], "create", "action is not create")
        self.assertIn("object_type", tokens, "object_type not set")
        self.assertEqual(tokens["object_type"], "table")


if __name__ == "__main__":
    unittest.main()
