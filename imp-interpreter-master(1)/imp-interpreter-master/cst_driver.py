from imp_lexer import *
from parser_cst import *
from anytree.exporter import DictExporter
from collections import OrderedDict
from anytree.importer import JsonImporter

import sys

input4_1 = '(+,3,(*,2,1))'
input4_2 = "(*,(-,3,5),(+,2,7))"
input4_3 = "(*,(-,(/,2,1),(*,1,0)),(+,2,8))"
input6_1 = r"n:=2;ans:=1;while (>=,n,1) do {ans:=ans+n;n:=n-1}"
input6_2 = r"n:=1; ans:=0;while (<=, n, 16) do {ans:=ans+n;n:=(*,2,n)}"

input_list = [input4_1, input4_2, input4_3, input6_1, input6_2]
input_desc = ["Problem 4 Example 1","Problem 4 Example 2","Problem 4 Example 3","Problem 6 Example 1","Problem 6 Example 2"]

for input, desc in zip(input_list,input_desc):
    print('',end = '\n\n')
    print(desc,end = '\n')
    print("Input String:")
    print(input,end = '\n\n')
    print("Tokens:")
    tokens = imp_lex(input)
    print(tokens,end = '\n\n')

    print("CST Data Structure:")
    
    # CST Parser
    parser = Parser(tokens)
    parser.parser_cst()
    parser.print_tree()
    parser.export_tree(desc+'.json')

importer = JsonImporter()

with open("Problem 4 Example 1.json") as filehandle:
    tree = importer.read(filehandle)

print(RenderTree(tree))