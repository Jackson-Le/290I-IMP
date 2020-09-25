from sly import Lexer

class TokenLexer(Lexer):
    tokens = { VARS, NUMBERS }
    ignore = '\t '
    literals = {'=', '+', '-', '/', '*', '/', '(', ')', ',', ';'}

    VARS = r'[a-zA-Z_][a-zA-Z\d_]'
    #COMS = r'[(if)*(else)*(while)*(then)*]+'

    @_(r'\d+')
    def NUMBERS(self, val):
        val.value = int(val.value)
        return val
