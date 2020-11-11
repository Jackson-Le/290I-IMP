# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:20:56 2020
Assignement #2
Problem #5
CE 290I Fall 2020
Group 4
Alvin & Nick

"""
#Tree Walking function that takes AST as input and walks through nodes and solves ast.
#Current code set up where name and value are in terminal node.
def asteval(ast): 
    # from anytree.importer import DictImporter
    # importer = DictImporter()
    # ast=importer.import_(ast)
    #ast=list()
    # from anytree import Node, RenderTree
    if ast.kw=='INT':
        return int(ast.val)
    if ast.kw=='FLOAT':
        return float(ast.val)
    if ast.kw=='RESERVED':
        if ast.val=='+':
            return asteval(ast.children[0])+asteval(ast.children[1])
        if ast.val=='-':
            return asteval(ast.children[0])-asteval(ast.children[1])
        if ast.val=='*':
            return asteval(ast.children[0])*asteval(ast.children[1])
        if ast.val=='/':
            return asteval(ast.children[0])/asteval(ast.children[1])