# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:09:51 2020
Assignement #2
Problem #3
CE 290I Fall 2020
Group 4
Alvin & Nick
"""
#Tree Walking function that takes CST as input and walks through Arithmetic nodes and prints character results
#Current code set up where name and value are in terminal node. If value is name of next node, then code needs to be modified.
def cstwalk(cst): 

    if cst.name[-4:]=='Aexp':
        print(cst.name[-4:])
        for i in range(len(cst.children)):
            
            #Recursively call CST parser for additional expressions in tree
            if cst.children[i].name[-4:]=='Aexp':
               cstwalk(cst.children[i])
               continue
            
            if cst.children[i].kw=='RESERVED':
                print(cst.children[i].kw)
                print(cst.children[i].val)
                
            if cst.children[i].kw=='INT' or cst.children[i].kw=='FLOAT':
                print(cst.children[i].kw)
                print(cst.children[i].val)

    #If name of node is not an Aexp, print an error
    if cst.name[-4:]!='Aexp':
        print('Code Not Ready for non-Arithmetic Expressions!')