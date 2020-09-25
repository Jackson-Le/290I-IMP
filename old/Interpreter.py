import Lexer
import Parser
import Execute

if __name__ == '__main__':
    lexer = Lexer.TokenLexer()
    parser = Parser.Parser()
    print('IMP Language')
    env = {}

    while True:

        try:
            text = input('IMP Language > ')

        except EOFError:
            break

        if text:
            tree = parser.parse(lexer.tokenize(text))
            Execute.Interpret(tree, env)
