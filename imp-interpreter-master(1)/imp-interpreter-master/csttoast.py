# -*- coding: utf-8 -*-
"""

Created on Sat Sep 26 15:09:51 2020
Assignement #2
Problem --
CE 290I Fall 2020
Group 4
Alvin & Nick
"""

#Tree Walking function that takes CST as input and walks through Arithmetic nodes and creates AST, then solves AST.
#Current code set up where name and value are in terminal node. If value is name of next node, then code needs to be modified.
def csttoast(cst): 
   
#    from anytree import Node, RenderTree
    
    from anytree import findall_by_attr, RenderTree
    Par=findall_by_attr(cst,'(','val')+findall_by_attr(cst,')','val')
    
    for i in range(len(Par)):
        Par[i].parent=None        

    # if cst.name[-3:]='Com':


    if cst.name[-4:]=='Aexp':
        if len(cst.children)==1:
            cst=cst.children[0]
        else:
        
            i=0
            while i<=(len(cst.children)-1):
                #print(root.children[i].name[-1:])
                #Recursively call CST parser for additional expressions in tree
             
                if cst.children[i].kw=='RESERVED':
                    if i==0:
                        cst.children[i].children=cst.children[1:]
                        cst=cst.children[i]
                
                if cst.children[i].kw=='INT' or cst.children[i].kw=='FLOAT' or cst.children[i].kw=='ID':
                    pass
                
                if cst.children[i].name[-4:]=='Aexp':
                    if i==0:
                        cst.children=[csttoast(cst.children[i]),cst.children[i+1]]
                    if i==1:
                        cst.children=[cst.children[i-1],csttoast(cst.children[i])]
                
                i=i+1

    # print('Exit Function')
    return cst
    # print(RenderTree(cst))
    
    # from collections import OrderedDict
    
    # exporter_dict = DictExporter(dictcls=OrderedDict, attriter=sorted)
    # return(exporter.export(cst))

    # exporter_json = JsonExporter(indent=2, sort_keys=True)
    # with open(filename,'w') as filehandle:
    #     exporter_json.write(cst,filehandle)
    # print('CST tree export to JSON successful!')
    
    
