import re

class Lexer:
    def __init__(self, to_tokenize):
        self.to_tokenize = to_tokenize.replace(" ", "")

    tokens = {"AExp": r'(:=)*[\+\-\/\*]*',
              "BExp": r'(<=)*(>=)*(==)*[<>]*(or)*(and)*',
              "Com": '(if)*(else)*(while)*(then)*',
              "Var": ''}

    def search_tokens(value):
        token_locations = []
