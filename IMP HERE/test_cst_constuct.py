from imp_lexer import *
from construct_cst import *

x = imp_lex('(+,(-,3,1),(*,2,1))')
y = imp_lex('(+,3,(*,2,1))')
z = imp_lex('(+,(-,3,1),1)')
i = imp_lex('(+,2,3)')
n3 = imp_lex('(*,(-,(/,2,1),(*,1,0)),(+,2,8))')
n2 = imp_lex('(*,(-,3,5),(+,2,7))')
n1 = imp_lex('(-,(*,3,9),4)')
e = imp_lex('n:=1')
e1 = imp_lex('n:=(+,2,3);ans:=(-,n,1)')
inter = imp_lex('n:=(+,ans,n)')
while_loop = imp_lex('while(>=,n,1)do{ans:=(+,ans,n);n:=(-,n,1)}')
while_loop1 = imp_lex('n:=2;ans:=1;while(>=,n,1)do{ans:=(+,ans,1);n:=(-,n,1)}')
while_loop2 = imp_lex('n:=2;ans:=0;while(<=,n,16)do{ans:=(+,ans,n);n:=(*,2,n)}')
bool = imp_lex('(>=,n,1)')
test = imp_lex('ans:=(+,ans,n);n:=(*,2,n)')

if1 = imp_lex('if(true)then{ans:=1}')
if2 = imp_lex('if(false)then{ans:=1}else{ans:=0}')
if3 = imp_lex('if(false)then{ans:=1}elif(true)then{ans:=0}')
if4 = imp_lex('if(false)then{ans:=1}elif(false)then{ans:=0}elif(true)then{ans:=2}')
if5 = imp_lex('if(false)then{ans:=1}elif(false)then{ans:=0}else{ans:=2}')
if6 = imp_lex('if(false)then{ans:=1}elif(false)then{ans:=0}elif(true)then{ans:=3}else{ans:=2}')

simple_else = imp_lex('n:=2;ans:=0;if(>,n,1)then{ans:=(+,ans,1)}else{ans:=(-,ans,1)}')
else_if = imp_lex('n:=2;ans:=0;if(>,n,1)then{ans:=(+,ans,1)}elif(<=,n,1)then{ans:=(-,ans,1)}')
else_if_else = imp_lex('n:=2;ans:=0;if(>,n,2)then{ans:=(+,ans,1)}elif(<,n,2)then{ans:=(-,ans,1)}else{ans:=2}')


#print('this is x:')
xx = buildCST(x)

#print('this is y:')
yy = buildCST(y)

#print('this is z:')
zz = buildCST(z)

#print('this is i:')
ii = buildCST(i)

nn1 = buildCST(n1)

ee1 = buildCST(e)
ee2 = buildCST(e1)

bool1 = buildCST(bool)
w1 = buildCST(while_loop)
inter1 = buildCST(while_loop)

wl1 = buildCST(while_loop1)
wl2 = buildCST(while_loop2)

test1 = buildCST(test)
#print(inter[2:9])

if_1 = buildCST(if1)
print('1 single if case situation')
treeWalker(if_1)

if_2 = buildCST(if2)
print('2 single if-else case situation')
treeWalker(if_2)

if_3 = buildCST(if3)
print('3 single if-elif case situation')
treeWalker(if_3)

if_4 = buildCST(if4)
print('4 single if-elif-elif case situation')
treeWalker(if_4)

if_5 = buildCST(if5)
print('5 single if-elif-else case situation')
treeWalker(if_5)

if_6 = buildCST(if6)
print('6 single if-elif-elif-else case situation')
treeWalker(if_6)

def treeWalker(tree, depth = 0):
    if type(tree.value) != str:
        print(tree.type)#, '\t \t depth:', depth)
        for node in tree.children:
            treeWalker(node)#, depth + 1)
    elif tree.value == 'if' or tree.value == 'elif' or tree == 'else':
        print(tree.value)#, '\t \t depth:', depth)
        for node in tree.children:
            treeWalker(node)
    else:
        print(tree.type)#, '\t \t depth:', depth + 1)
        print(tree.value)#, '\t \t depth:', depth + 1)

#treeWalker(ee1)





#print('Bool test')
#treeWalker(bool1, 0)

#treeWalker(test1)
#print('while loop: n:=2;ans:=1;while(>=,n,1)do{ans:=(+,ans,1);n:=(-,n,1)}')
#treeWalker(wl1, 0)
#print('while loop: n:=2;ans:=0;while(<=,n,16)do{ans:=(+,ans,n);n:=(*,2,n)}')
#treeWalker(wl2, 0)
#treeWalker(ee1)
#print(e1)
#treeWalker(w1)
#treeWalker(inter1)
#print(makeBexp(bool))
#treeWalker(makeBexp(bool))
#treeWalker(nn1)

#treeWalker(w1)
