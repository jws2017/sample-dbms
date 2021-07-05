import sys
import tokenizer
import database_manager

def main():
    manager = database_manager.DatabaseManager()
    while True:
        text = input("SQL >> ")
        if not text:
            break
        if ';' in text:
            text = text[:text.find(';')]
        try:
            print(tokenizer.interpret(manager, tokenizer.tokenize(text)))
        except NotImplementedError:
            print("That is not a valid SQL command. Please try again.")
            continue
    return 0

if __name__ == "__main__":
    sys.exit(int(main() or 0))