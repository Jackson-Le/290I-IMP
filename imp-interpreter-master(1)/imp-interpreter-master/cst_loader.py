import sys
from anytree.importer import JsonImporter
from anytree import *



if __name__ == '__main__':
    filename = sys.argv[1]
    importer = JsonImporter()
    with open(filename) as filehandle:
        tree = importer.read(filehandle)

    print(filename + ' Tree',end='\n\n')
    print(RenderTree(tree))