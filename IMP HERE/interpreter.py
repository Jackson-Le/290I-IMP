from ast import *

def interpret(node):
    totals = []
    if node.type == 'OPERATOR': #and node.value == '+':
        for i in range(len(node.children)):

            #Check if child is also an operator and, if so, call function again
            if node.children[i].type == 'OPERATOR':
                interpret(node.children[i])

            #Convert all INT values into intergers
            if node.children[i].type == 'INT':
                node.children[i].value = int(node.children[i].value)
                totals.append(node.children[i].value)

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
