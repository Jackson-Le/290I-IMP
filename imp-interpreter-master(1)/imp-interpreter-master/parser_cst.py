# Alvin Zhou, Nicholas Strella
# CE290I
# Fall 2020


# Parser to transform lexer tokens from modified IMP syntax to CST
# Function takes in a list of token tuples in the form of ('TOKEN CHAR', 'KEYWORD')
# Keywords are RESERVED, INT, ID

# If successful, returns a CST in a tree format
from anytree import *
from anytree.exporter import DictExporter
from collections import OrderedDict
from anytree.exporter import JsonExporter
import re
import pdb

class Parser():
    def __init__(self, token_stream):
        self.pos = 0
        self.token_stream = token_stream
        self.level = 0
        self.nest = OrderedDict()
        self.add_elseif = False

    def parser_cst(self):
        
        def nest_logic(current_token,current_token_kw):

            return


        def root_logic(current_token, current_token_kw):
            # Function to create a root node of the appropriate type

            
            aexp_op = r'[\+\*/-]'
            bool_opword = r'or|and|not'
            bool_standalone = r'not|true|false'
            bool_op = r'<|<=|>|>=|==|!='
            com_start = r'^if|while|skip'
            com_cond = r'^if|while|elseif'
            
            # Default to None if nothing works
            parent = None

            # Don't search if it's the last token
            try:
                next_token = self.token_stream[self.pos+1][0]
                next_token_kw = self.token_stream[self.pos+1][1]
            except:
                if current_token_kw == 'RESERVED':
                    return
                pass 

            # An aexp with a left parentheses will have an arithmetic operator, a number, or a variable
            if current_token_kw == 'RESERVED':
                if current_token == '(': # Match for (paren, op) only
                # Check for aexp, bexp, or com using the next token
                    if re.search(aexp_op, next_token):  # Match any arithmetic op
                        parent = Node('Aexp', kw = '',val='')
                    elif re.search(bool_op, next_token):
                        parent = Node('Bexp', kw = '',val='')
                    elif re.search(bool_opword, next_token):
                        parent = Node('Bexp', kw = '',val='')
                    if re.search(bool_standalone, current_token):
                        parent = Node('Bexp', kw = '',val='')
                elif re.search(com_start, current_token):
                    parent = Node('Com', kw = '',val='')
                elif re.search(bool_standalone, current_token):
                    parent = Node('Bexp', kw = '',val='')
                elif re.search(com_cond, current_token):
                    parent = Node('Com', kw = '',val='')
                # Add com case

            if current_token_kw == 'ID':
                if next_token == ':=':
                    child = None
                    #child = Node('Aexp',kw = '', val = '')
                    parent = Node('Com', children = child,kw = '',val='')
                else:
                    parent = Node('Aexp', kw = '',val='')

            if current_token_kw == 'INT': 
                parent = Node('Aexp', kw = '',val='')
            
            if current_token_kw == 'FLOAT':
                parent = Node('Aexp', kw = '',val='')
            
            if not(parent is None):
                self.flag_token = current_token
                self.level += 1
            return parent

        if self.pos > 0:
            print('Warning: Tokens have already been parsed')

        # Main loop
        while self.pos < len(self.token_stream):

            current_token = self.token_stream[self.pos][0]
            current_token_kw = self.token_stream[self.pos][1]
            
            # Define root node
            if self.pos == 0:
                current_root = root_logic(current_token, current_token_kw)
                Node(current_token, parent = current_root, children = None, kw = current_token_kw, val = current_token)
                self.cst = current_root
                self.pos += 1
                continue
            
            # Determine if a new root results from expression
            new_root = root_logic(current_token,current_token_kw)

            # If the token represents the start of an expression, create a new root node to add children to
            if not(new_root is None):
                new_root.parent = current_root
                current_root = new_root # Move down a level in tree    

            # Add node to parent node
            new_node = Node(current_token, parent = current_root, children = None, kw = current_token_kw, val = current_token)

            if current_token == '{':
                self.nest[new_node.name] = new_node.parent
            #print(RenderTree(self.cst))
            
            # Logic after adding node to decide level to place next node
            token_exclude = r"[\{\(\+\*/]|<|<=|>|>=|==|!=|^if$|while|then|do|^else$|:=|-$|;"
            token_raise = r"[\),\}]"
            kw_exclude = r"ID"

            if self.level>0:               
                if re.match(token_exclude,current_token):
                    pass
                elif re.match(kw_exclude,current_token_kw):
                    if new_root.name[-3:] == 'Com':
                        pass
                    else:
                        current_root = current_root.parent
                        self.level+=1
                elif current_token =="}": # Special case for nested if/while blocks
                    (_,parent) = self.nest.popitem()
                    new_node.parent = parent
                else:
                    current_root = current_root.parent
                    self.level += -1
                pass

            self.pos += 1
        return
    
    def print_tree(self):
        print(RenderTree(self.cst),end='\n\n\n')
        return
    
    def export_tree(self,filename):
        exporter_dict  = DictExporter(dictcls=OrderedDict, attriter=sorted)
        self.export_cst_dict = exporter_dict.export(self.cst)

        exporter_json = JsonExporter(indent=2, sort_keys=True)
        with open(filename,'w') as filehandle:
            exporter_json.write(self.cst,filehandle)
        
        print('CST tree export to JSON successful!')
        return
