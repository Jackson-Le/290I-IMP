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
            tree = imp_parse(imp_lex(text))
            ast = tree.values
            ast.eval(env)
