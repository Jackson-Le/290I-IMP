# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 13:47:05 2020

@author: temp
"""

#This Next module uses anytree to create tree structures with parents and children

#copy & paste this command in your command line to download the anytree library package
#pip install anytree

#Load functions we will be using
from anytree import Node, RenderTree

#Try: 2+3

#This first code writes tree where Operator and Num types are terminals
root=Node('Aexp')
Op1=Node('#',parent=root,val='+')
Left1=Node('n',parent=root,val='2')
Right1=Node('n',parent=root,val='3')
print(RenderTree(root))

#This second code writes tree where Operator and Num types have sub-nodes that are terminal
root2=Node('Aexp')
Op1=Node('#',parent=root2)
Left1=Node('n',parent=root2)
Right1=Node('n',parent=root2)
Op2=Node('+',parent=Op1)
Left2=Node('2',parent=Left1)
Right2=Node('3',parent=Right1)

print(RenderTree(root2))


#Try: (2+3)*(15+-6)

# This expands the tree to additional operators using the sytax sim to root
root3=Node('Aexp')
Op1=Node('#',parent=root3,val='*')
Left1=Node('Aexp',parent=root3)
Right1=Node('Aexp',parent=root3)
Op2=Node('#',parent=Left1,val='+')
Left2=Node('n',parent=Left1,val='2')
Right2=Node('n',parent=Left1,val='3')
Op3=Node('#',parent=Right1,val='+')
Left3=Node('n',parent=Right1,val='15')
Right3=Node('n',parent=Right1,val='-6')


print(RenderTree(root3))