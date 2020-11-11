from imp_lexer import *
from parser_cst import *
import sys

if __name__ == '__main__':
    print()
    input = sys.argv[1] 
    print("Input String:")
    print(input,end = '\n\n')
    tokens = imp_lex(input)
    print("Tokens:")
    print(tokens,end='\n\n')

     #CST Parser
    parser = Parser(tokens)
    parser.parser_cst()
    print("CST Data Structure:")
    parser.print_tree()