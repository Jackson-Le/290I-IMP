from construct_cst import *
from construct_ast import *

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
            if node.children[i].type != 'INT' and node.children[i].type != 'ID':
                interpret(node.children[i])
                value = node.children[i].value
            if node.children[i].bool != None:
                interpret(node.children[i])
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
    
    if node.type == 'COMS' and node.value == 'if':
        condition = None
        for i in range(len(node.children)):
            if node.children[i].type == 'BOOLEAN':
                interpret(node.children[i])
                condition = node.children[i].bool 
        for i in range(len(node.children)):
            if node.children[i].value != 'BOOLEAN' and condition == True:
                interpret(node.children[i])
        if condition == True:
            node.parent.bool = True
            
    if node.type == 'COMS' and node.value == 'elif' and node.parent.bool != True:
        condition = None
        node.parent.bool = None
        for i in range(len(node.children)):
            if node.children[i].type == 'BOOLEAN':
                interpret(node.children[i])
                condition = node.children[i].bool 
        for i in range(len(node.children)):
            if node.children[i].value != 'BOOLEAN' and condition == True:
                interpret(node.children[i])
        if condition == True:
            node.parent.bool = True
        print(node.parent.bool)

    if node.type == 'COMS' and node.value == 'else' and node.parent.bool != True:
        print('else!')
        for i in range(len(node.children)):
            interpret(node.children[i])    
                
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
        print(node.parent.value,'=', node.bool)
        
    if node.type == 'OPERATOR':
        for i in range(len(node.children)):
            if node.children[i].type == 'OPERATOR':
                interpret(node.children[i])
            if node.children[i].type == 'INT' or type(node.children[i].value) == int or type(node.children[i].value) == float:
                node.children[i].value = int(node.children[i].value)
                totals.append(node.children[i].value)
            if node.children[i].type == 'ID':
                totals.append(var[node.children[i].value])

        if  node.bool == '+':
            for j in range(len(totals)-1):
                node.value = totals[0]
                node.value += totals[j+1]
        elif node.bool =='-':
            for j in range(len(totals)-1):
                node.value = totals[0]
                node.value -= totals[j+1]
        elif node.bool =='*':
            for j in range(len(totals)-1):
                node.value = totals[0]
                node.value *= totals[j+1]
        elif node.bool =='/':
            for j in range(len(totals)-1):
                node.value = totals[0]
                node.value /= totals[j+1]

'''
while_loop1 = buildCST(imp_lex('n:=2;ans:=1;while(>=,n,1)do{ans:=(+,ans,1);n:=(-,n,1)}'))
while_loop2 = buildCST(imp_lex('n:=2;ans:=0;while(<=,n,16)do{ans:=(+,ans,n);n:=(*,2,n)}'))

ast(while_loop1)
interpret(while_loop1)
print(var)
var = {}

ast(while_loop2)
interpret(while_loop2)
print(var)
var = {}
'''
simple_else = buildCST(imp_lex('n:=2;ans:=0;if(>,n,1)then{ans:=(+,ans,1)}else{ans:=(-,ans,1)}'))
else_if = buildCST(imp_lex('n:=2;ans:=0;if(>,n,1)then{ans:=(+,ans,1)}elif(<=,n,1)then{ans:=(-,ans,1)}'))
else_if_else = buildCST(imp_lex('n:=2;ans:=0;if(>,n,2)then{ans:=(+,ans,1)}elif(<,n,2)then{ans:=(-,ans,1)}else{ans:=2}'))

'''
ast(simple_else)
interpret(simple_else)
print(var)
var = {}

ast(else_if)
interpret(else_if)
print(var)
var = {}
ast(else_if_else)
interpret(else_if_else)
print(var)
'''
