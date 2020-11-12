from lexer import *
from cst import *

def properlyBuilt(tokens):
    if type(tokens) != list:
        return False
    if tokens[0] == ('(', 'TERMINAL') and tokens[-1] == (')', 'TERMINAL'):
        return True
    else:
        return False

def findAExp(tokens):
    counter = 0
    if tokens[0][0] == '(':
        for i in range(len(tokens)):
            if tokens[i][0] == '(':
                counter += 1
            elif counter <= 0:
                return (tokens[:i],i)
            elif tokens[i][0] == ')':
                counter -= 1
    return (tokens[0],1)

def buildCST(tokens):
    if properlyBuilt(tokens):
        operation = tokens[1]
        operator = Node(value = operation, type = "OPERATOR")
        nodes_id = findAExp(tokens[3:])
        left = nodes_id[0]
        if type(left) == list and len(left) > 1:
            # Lnode is the node that we have made for the left side of the tree
            Lnode = Node(value = left, type = 'Aexp')
            opLnode = buildCST(left[1]) # operator of l node_1
            Lnode.add_child(opLnode)
            # Lnodes_id is the AExp finding function that returns tokens and the length of the tokens
            Lnodes_id = findAExp(Lnode.value[3:])
            LLnode = buildCST(Lnodes_id[0]) # recursively builds CST node
            pointer = Lnodes_id[1]
            Lnode.add_child(LLnode) # this builds left side
            Lremaining_tokens = Lnode.value[pointer+4:]
            Lnodes_id = findAExp(Lremaining_tokens)
            LRnode = buildCST(Lnodes_id[0]) # recursively builds CST node
            Lnode.add_child(LRnode) # this builds right side
        elif type(left) == tuple:
            Lnode = Node(value = left[0], type = left[1])
        else:
            Lnode = Node(value = left, type = 'INT') # if AExp is singular
        pointer = nodes_id[1]
        remaining_tokens = tokens[pointer+4:]
        right = findAExp(remaining_tokens)[0]
        if type(right) == list and len(right) > 1:
            # Rnode is the node that we have made for the left side of the tree
            Rnode = Node(value = right, type = 'Aexp')
            opRnode = buildCST(remaining_tokens[1]) # operator of r node_1
            Rnode.add_child(opRnode)
            # Rnodes_id is the AExp finding function that returns tokens and the length of the tokens
            Rnodes_id = findAExp(Rnode.value[3:])
            RLnode = buildCST(Rnodes_id[0])
            pointer = Rnodes_id[1]
            Rnode.add_child(RLnode) # this builds left side
            Rremaining_tokens = Rnode.value[pointer+4:]
            Rnodes_id = findAExp(Rremaining_tokens)
            RRnode = buildCST(Rnodes_id[0])
            Rnode.add_child(RRnode) # this builds right side
        elif type(right) == tuple:
            Rnode = Node(value = right[0], type = right[1])
        else:
            Rnode = Node(value = right, type = 'INT') # if AExp is singular
    else:
        return Node(value = tokens[0], type = tokens[1])
    starter_node = Node(value = tokens, type = 'Aexp', children = [operator, Lnode, Rnode])
    operator.update_parent(starter_node)
    Lnode.update_parent(starter_node)
    Rnode.update_parent(starter_node)
    return  starter_node
