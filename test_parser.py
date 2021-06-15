import tokenizer

if __name__ == "__main__":
    print(tokenizer.tokenize(""))
    print(tokenizer.tokenize("CREATE TABLE table;"))
    print(tokenizer.tokenize("CREATE assignment_database;"))
    print(tokenizer.tokenize("CREATE dd"))