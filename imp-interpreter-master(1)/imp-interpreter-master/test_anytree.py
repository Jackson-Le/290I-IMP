from anytree import Node, RenderTree
import pdb
a = Node('b')
Node('a',parent = a)
Node('b',parent = a)
Node('c',parent = a)
Node('d',parent = a)
b = a.children[0]
a = Node('b_child',parent=b)
Node('e', parent = b)
a = b.parent
print(RenderTree(a))
pdb.set_trace()