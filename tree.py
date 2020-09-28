#Printing the nodal tree for problem 2:

class tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level


    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces+ '|__' if self.parent else ''

        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self,child):
        child.parent = self
        self.children.append(child)


def build_tree(class_name):
    root0 = class_name('a')

    op1 = class_name('(+)')
    t2_op1 = class_name('+')
    op1.add_child(t2_op1)

    n1 = class_name('n')
    t2_n1 = class_name('3')
    n1.add_child(t2_n1)

    a1 = class_name('a')
    op2_a1 = class_name('(+)')
    n2_0_a1 = class_name('n')
    n2_1_a1 = class_name('n')
    op3_a1 = class_name('*')
    n3_0_a1 = class_name('2')
    n3_1_a1 = class_name('1')
    op2_a1.add_child(op3_a1)
    n2_0_a1.add_child(n3_0_a1)
    n2_1_a1.add_child(n3_1_a1)
    a1.add_child(op2_a1)
    a1.add_child(n2_0_a1)
    a1.add_child(n2_1_a1)

    root0.add_child(op1)
    root0.add_child(n1)
    root0.add_child(a1)

    root0.print_tree()

build_tree(tree)
