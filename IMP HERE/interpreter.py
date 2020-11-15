from ast import *

var = {}
def interpret(node):
    totals = []
    if node.type == 'COMS' and type(node.value) == list:
        for i in range(len(node.children)):
            interpret(node.children[i])
            
    if node.type == 'COMS' and node.value == ':=':
        key = None
        value = None
        for i in range(len(node.children)):
            if node.children[i].type == 'ID':
                key = node.children[i].value
            if node.children[i].type == 'INT':
                node.children[i].value = int(node.children[i].value)
                value = node.children[i].value
        var[key] = value
                
    if node.type == 'COMS' and node.value == 'while':
        condition = None
        for i in range(len(node.children)):
            if node.children[i].type == 'BOOLEAN':
                interpret(node.children[i])
                condition = node.children[i].bool 
        for i in range(len(node.children)):
            if node.children[i].value != 'BOOLEAN' and condition == True:
                interpret(node.children[i])
        if condition == True:
            interpret(node)
                
    if node.type == 'BOOLEAN':
        left  = None
        right = None
        for i in range(len(node.children)):          
            if node.children[i].type == 'INT':
                node.children[i].value = int(node.children[i].value)
                if i == 0:
                    left = node.children[i].value
                if i == 1:
                    right = node.children[i].value
            
            if node.children[i].type == 'ID':
                if i == 0:
                    left = var[node.children[i].value]
                if i == 1:
                    right = var[node.children[i].value]

        node.bool = False
        if  node.value == '<=':
            if left <= right:
                node.bool = True
        elif node.value =='<':
            if left < right:
                node.bool = True
        elif node.value =='>=':
            if left >= right:
                node.bool = True
        elif node.value =='>':
            if left > right:
                node.bool = True
        elif node.value =='==':
            if left == right:
                node.bool = True
        elif node.value =='!=':
            if left != right:
                node.bool = True
        
    
    if node.type == 'OPERATOR': #and node.value == '+':
        for i in range(len(node.children)):
            #Check if child is also an operator and, if so, call function again
            if node.children[i].type == 'OPERATOR':
                interpret(node.children[i])

            #Convert all INT values into intergers
            if node.children[i].type == 'INT':
                node.children[i].value = int(node.children[i].value)
                totals.append(node.children[i].value)
            
            if node.children[i].type == 'ID':
                totals.append(var[node.children[i].value])

        # Execute the Operation
        if  node.value == '+':
            print('+',totals)
            for j in range(len(totals)-1):
                node.value = totals[0]
                node.value += totals[j+1]
                node.type = 'INT'
        elif node.value =='-':
            print('-',totals)
            for j in range(len(totals)-1):
                node.value = totals[0]
                node.value -= totals[j+1]
                node.type = 'INT'
        elif node.value =='*':
            print('*',totals)
            for j in range(len(totals)-1):
                node.value = totals[0]
                node.value *= totals[j+1]
                node.type = 'INT'
        elif node.value =='/':
            for j in range(len(totals)-1):
                node.value = totals[0]
                node.value /= totals[j+1]
                node.type = 'INT'