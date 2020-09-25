from sly import Parser
import Lexer
class Parser(Parser):
    tokens = Lexer.TokenLexer.tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),
    )

    def __init__(self):
        self.env = {}

    @_('')
    def statement(self, input):
        pass

    @_('assignment')
    def statement(self, input):
        return input.assignment

    @_('VARS "=" expr')
    def assignment(self, input):
        return ('=', input.VARS, input.expr)

    @_('expr')
    def statement(self, input):
        return (input.expr)

    @_('expr "+" expr')
    def expr(self, input):
        return ('+', input.expr0, input.expr1)

    @_('expr "-" expr')
    def expr(self, input):
        return ('-', input.expr0, input.expr1)

    @_('expr "*" expr')
    def expr(self, input):
        return ('*', input.expr0, input.expr1)

    @_('expr "/" expr')
    def expr(self, input):
        return ('/', input.expr0, input.expr1)

    @_('"-" expr %prec UMINUS')
    def expr(self, input):
        return input.expr

    @_('VARS')
    def expr(self, input):
        return ('VARS', input.VARS)

    @_('NUMBERS')
    def expr(self, input):
        return ('NUMBERS', input.NUMBERS)
