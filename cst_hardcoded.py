from imp_lexer import *

class Terminal:
    def __init__(self, data, type):
        self.data = data
        self.type = type

    def to_string():
        print(self.type)
        print(self.data)

class Aexp:
    def __init__(self, operater, left, right):
        self.operater = operater
        self.left = left
        self.right = right

    def to_string():
        print(self.data)

class Group:
    def __init__(self, left, exp, right):
        self.exp = exp
        self.left = left
        self.right = right

    def to_string():
        print(self.exp)

def makeTerminal(item):
    return Terminal(item[0], item[1])

base_question = imp_lex('(+,3,(*,2,1))')

Second_Aexp = Aexp(makeTerminal(base_question[6]),
                   makeTerminal(base_question[8]),
                   makeTerminal(base_question[10]))

Second_group = Group(makeTerminal(base_question[5]),
                     Second_Aexp,
                     makeTerminal(base_question[11]))

First_Aexp = Aexp(makeTerminal(base_question[1]),
                  makeTerminal(base_question[3]),
                  Second_Aexp)

First_group = Group(makeTerminal(base_question[0]),
                     First_Aexp,
                     makeTerminal(base_question[12]))

def treeWalker(tree):
    if type(tree) == Terminal:
        print(tree.type)
        print(tree.data)
    elif type(tree) == Group:
        print(type(tree))
        treeWalker(tree.exp)
    elif type(tree) == Aexp:
        print(type(tree))
        treeWalker(tree.operater)
        treeWalker(tree.left)
        treeWalker(tree.right)

treeWalker(First_group)
