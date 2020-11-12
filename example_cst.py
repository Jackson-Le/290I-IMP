from cst import *
from imp_lexer import *

base_question = imp_lex('(+,3,(*,2,1))')

node_1 = Node(value = '1', type = 'INT')
node_2 = Node(value = '2', type = 'INT')
node_times = Node(value = '*', type = 'OPERATOR')
secondAexp = Node(base_question[5:11], 'Aexp', None, [node_times, node_2, node_1])
node_3 = Node(value = '3', type = 'INT')
node_plus = Node(value = '+', type = 'OPERATOR')
firstAexp = Node(base_question, 'Aexp', None, [node_plus, node_3, secondAexp])

node_1.update_parent(secondAexp)
node_2.update_parent(secondAexp)
node_times.update_parent(secondAexp)

secondAexp.update_parent(firstAexp)
node_3.update_parent(firstAexp)
node_plus.update_parent(firstAexp)
