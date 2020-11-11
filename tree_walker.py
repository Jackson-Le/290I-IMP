from tree import tree
from tree import build_tree

class walk_the(tree):
    def print_tree(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

build_tree(walk_the)
