'''
    Desenvolvido por:
        - Lucas Zortea
        - Marcelo Dalvi
        - Rhayane Fabres
        - Victor Rosa
'''

import os
from nodeABB import NodeABB

if __name__ == '__main__':
    
    clear = lambda: os.system('cls')
    clear()
    
    def menu_options():
        pass

    def altura(arbin:NodeABB):
        if arbin is None:
            return -1
        else:
            alturaEsquerda = altura(arbin.esqArbin())
            alturaDireita = altura(arbin.dirArbin())
        if alturaEsquerda > alturaDireita:
            return alturaEsquerda + 1
        else:
            return alturaDireita + 1

    def preOrder(node:NodeABB):
        if node is not None:
            print(node._data, end=" ")
            preOrder(node._esq)
            preOrder(node._dir)
    
    def inOrder(node:NodeABB):
        if node is not None:
            inOrder(node._esq)
            print(node._data, end=" ")
            inOrder(node._dir)
            
    def posOrder(node:NodeABB):
        if node is not None:
            posOrder(node._esq)
            posOrder(node._dir)
            print(node._data, end=" ")

    def inLevel(node:NodeABB, level):
        if node is not None:
            if level == 1:
                print(node._data,end=" ")
            elif level > 1:
                inLevel(node._esq, level - 1)
                inLevel(node._dir, level - 1)
    
    def open_file():
        file = open("C:\\Users\Victo\dev\estrutura-dados-python\\treeBinarySearchJob\\numbers-tree.txt")
        first_node = int(file.readline().rstrip())
        tree = NodeABB(first_node)
        
        for line in file:
            node = NodeABB(int(line.rstrip()))
            tree.add(node)
        file.close()

        return tree

    def view_tree(tree:NodeABB):
        if (tree):
            print(f'{tree._data}',end= " ")
            view_tree(tree.esqArbin())
            view_tree(tree.dirArbin())

    def view_routes(tree:NodeABB):
        
        preOrder(tree)
        # in-order
        # pos-order
        # levels
        pass
        
    tree = open_file()
    print("Arvore Binária")
    view_tree(tree)

    print("\n")
    print("pre-order")
    preOrder(tree)

    print("\n")
    print("in-order")
    inOrder(tree)

    print("\n")
    print("pos-order")
    posOrder(tree)

    print("\n")
    print("in-level")
    varAltura = altura(tree)
    inLevel(tree, varAltura)