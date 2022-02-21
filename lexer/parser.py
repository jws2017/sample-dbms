import tokenizer

def parse(tokens: list[tokenizer.Token]):
    if tokenizer.KEYWORDS['select'] == tokens[0]:
        if tokens[1].type == 'identifier':
            pass
        raise SyntaxError
    raise SyntaxError
