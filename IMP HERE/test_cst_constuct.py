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


#print('this is x:')
#xx = buildCST(x)

#print('this is y:')
#yy = buildCST(y)

#print('this is z:')
#zz = buildCST(z)

#print('this is i:')
#ii = buildCST(i)

#nn1 = buildCST(n1)

#ee1 = buildCST(e)
#ee2 = buildCST(e1)

bool1 = buildCST(bool)
#w1 = buildCST(while_loop)
#inter1 = buildCST(while_loop)

wl1 = buildCST(while_loop1)
wl2 = buildCST(while_loop2)

#test1 = buildCST(test)
#print(inter[2:9])
def treeWalker(tree, depth):
    if type(tree.value) != str:
        print(tree.type, '\t \t depth:', depth)
        for node in tree.children:
            treeWalker(node, depth + 1)
    else:
        print(tree.type, '\t \t depth:', depth + 1)
        print(tree.value, '\t \t depth:', depth + 1)
print('Bool test')
treeWalker(bool1, 0)

#treeWalker(test1)
print('while loop: n:=2;ans:=1;while(>=,n,1)do{ans:=(+,ans,1);n:=(-,n,1)}')
treeWalker(wl1, 0)
print('while loop: n:=2;ans:=0;while(<=,n,16)do{ans:=(+,ans,n);n:=(*,2,n)}')
treeWalker(wl2, 0)
#treeWalker(ee1)
#print(e1)
#treeWalker(w1)
#treeWalker(inter1)
#print(makeBexp(bool))
#treeWalker(makeBexp(bool))
#treeWalker(nn1)

#treeWalker(w1)
