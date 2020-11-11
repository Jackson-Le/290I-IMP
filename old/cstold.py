from imp_lex import *
class Node:
    def __init__(self, tree):
        self.tree = tree
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def parseThrough(self):
        if type(i) == str:
            print i
            return None
        for i in range(1,len(self.tree)-1):
            if i[0] == '(':
                add_child(makeAexp())
            elif type(i) == tuple:
                add_child(i)

    def makeAexp():
        counter = 0
        if counter == 0 and
