import tokenizer

if __name__ == "__main__":
    print(tokenizer.tokenize(""))
    print(tokenizer.tokenize("CREATE TABLE thingy(col1 int, col2 string);"))
    print(tokenizer.tokenize("CREATE DATABASE assignment_database;"))
    print(tokenizer.tokenize("CREATE INDEX dd ON table(col1);"))