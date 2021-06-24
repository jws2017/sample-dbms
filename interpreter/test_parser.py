from tokenizer import tokenize

if __name__ == "__main__":
    print(tokenize(""))
    print(tokenize("CREATE TABLE thingy(col1 int, col2 string);"))
    print(tokenize("CREATE DATABASE assignment_database;"))
    print(tokenize("CREATE INDEX dd ON table(col1);"))
    print(tokenize("SELECT * FROM table WHERE value=\"thingy\";"))
    print(tokenize("update tet set col1=\"mexico\""))
