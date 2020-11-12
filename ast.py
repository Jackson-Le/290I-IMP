from imp_lexer import *
from construct_cst import *
from test_cst_constuct import *


def ast(node):
    delete=[]
    if node.type == 'Aexp':
        for i in range(len(node.children)):
            if node.children[i].type == 'OPERATOR':
                node.value = node.children[i].value
                node.type = node.children[i].type
                delete.append(i)
        for j in range(len(delete)):
            del(node.children[j])
        for i in range(len(node.children)):
            if len(node.children[i].children) > 1:
                ast(node.children[i])
