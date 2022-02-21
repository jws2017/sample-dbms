from tokenizer import Lexer

def main():
    for token in Lexer('CREATE DATABASE 434352 "asged"db;').tokenize():
        print(f"{token.name}\t{token.value}")
    return 0

if __name__ == '__main__':
    main()
