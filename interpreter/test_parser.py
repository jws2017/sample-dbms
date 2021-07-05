from tokenizer import tokenize
import unittest

class Test_tokenizer(unittest.TestCase):
    def test_tokenize(self):
        self.assertEqual(tokenize("USE database;"), {"action": "use", "database": "database"})
        self.assertEqual(tokenize("CREATE TABLE thingy(col1 int, col2 string);"), {'action': 'create', 'object_type': 'table', 'name': 'thingy'})
        self.assertEqual(tokenize("CREATE DATABASE assignment_database;"), {'action': 'create', 'object_type': 'database', 'name': 'assignment_database'})
        self.assertEqual(tokenize("CREATE INDEX dd ON table(col1);"), {'action': 'create', 'object_type': 'index', 'name': 'dd', 'on': 'table(col1)'})
        self.assertEqual(tokenize("SELECT * FROM table WHERE value=\"thingy\";"), {'action': 'select', 'columns': '* ', 'table': 'table WHERE value="thingy"'})
        self.assertEqual(tokenize("update tet set col1=\"mexico\""), {'action': 'update', 'table': 'tet'})

if __name__ == "__main__":
    unittest.main()
