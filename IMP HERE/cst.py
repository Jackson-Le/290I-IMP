from imp_lexer import *

class Node:
    def __init__(self, value, type, parent = None, children = []):
        self.value = value
        self.type = type
        self.parent = parent
        self.children = children
        self.bool  = None        
        for i in children:
            i.update_parent(self)

    def to_string():
        print(value)

    def add_child(self, node):
        self.children.append(node)
        #print(self.type,":",self.value, "has added", node.type, ':', node.value)
            #node.update_parent(parent = self)

    def update_parent(self, parent):
        self.parent = parent

    def update_value(self, value):
        self.value = value

    # i values of 0 drop operater, 1 drops left node, 2 drops right node
    def remove_child(self, i):
        self.children = self.children[:i] + self.children[i+1:]
