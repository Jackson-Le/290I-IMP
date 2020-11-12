from IMPlexer import *
from IMPparser import *
from execute import *
from combinators import *
from IMPast import *

if __name__ == '__main__':
    print('IMP Language')
    env = {}

    while True:

        try:
            text = input('IMP Language > ')

        except EOFError:
            break

        if text:
            tokens = imp_lex(text)
            parse_result = imp_parse(tokens)
            ast = parse_result.value
            ast.eval(env)
