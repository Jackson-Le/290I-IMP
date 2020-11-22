from construct_cst import *

def ast(node):
    delete=[]    
    if node.type == 'AExp':
        for i in range(len(node.children)):
            if node.children[i].type == 'OPERATOR':
                node.value = node.children[i].value
                node.bool = node.value
                node.type = node.children[i].type
                delete.append(i)
        for j in range(len(delete)):
            del(node.children[delete[j]])
        for i in range(len(node.children)):
            if len(node.children[i].children) > 1:
                ast(node.children[i])
    
    if node.type == 'BExp':
        for i in range(len(node.children)):
            if node.children[i].type == 'BOOLEAN':
                node.value = node.children[i].value
                node.type = node.children[i].type
                delete.append(i)
        for j in range(len(delete)):
            del(node.children[delete[j]])
        for i in range(len(node.children)):
            if len(node.children[i].children) > 1:
                ast(node.children[i])
    
    if node.type == 'COMS':
        for i in range(len(node.children)):
            if node.children[i].value == ':=' or node.children[i].value == 'while':
                node.value = node.children[i].value
                node.type = node.children[i].type
                delete.append(i)
        for j in range(len(delete)):
            del(node.children[delete[j]])
        for i in range(len(node.children)):
            if len(node.children[i].children) >= 1:
                ast(node.children[i])
            

def ASTtreeWalker(tree):
    if type(tree.value) != str:
        print(tree.type)
        for node in tree.children:
            ASTtreeWalker(node)
    else:
        print(tree.value)
        for node in tree.children:
            ASTtreeWalker(node)