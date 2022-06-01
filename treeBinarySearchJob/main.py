
import os
from nodeABB import NodeABB
from arrayQueue import ArrayQueue

if __name__ == '__main__':
    
    clear = lambda: os.system('cls')
    clear()

    def pre_order(tree:NodeABB):
        if tree is not None:
            print(tree._data, end=" ")
            pre_order(tree._esq)
            pre_order(tree._dir)
    
    def in_order(tree:NodeABB):
        if tree is not None:
            in_order(tree._esq)
            print(tree._data, end=" ")
            in_order(tree._dir)
            
    def pos_order(tree:NodeABB):
        if tree is not None:
            pos_order(tree._esq)
            pos_order(tree._dir)
            print(tree._data, end=" ")

    def level_order(tree:NodeABB):
        queue = ArrayQueue()
        queue.enqueue(tree)
        
        while len(queue):
            tree = queue.dequeue()
            if tree._esq:
                queue.enqueue(tree._esq)
            if tree._dir:
                queue.enqueue(tree._dir)
            print(tree._data, end=" ")
    
    def height(tree:NodeABB):
        if tree is None:
            return -1
        else:
            height_left = height(tree.esqArbin())
            height_right = height(tree.dirArbin())
        if height_left > height_right:
            return height_left + 1
        else:
            return height_right + 1

    def view_tree(tree:NodeABB):
        if (tree):
            print(f'{tree._data}',end= " ")
            view_tree(tree.esqArbin())
            view_tree(tree.dirArbin())

    def view_routes(tree:NodeABB):
        print(f'pré-ordem: ',end="")
        pre_order(tree)

        print(f'\n')
        print(f'in-ordem: ',end="")
        in_order(tree)

        print(f'\n')
        print(f'pós-ordem: ',end="")
        pos_order(tree)

        print(f'\n')
        print(f'nível: ',end="")
        level_order(tree)

    def open_file(path):
        file = open("./treeBinarySearchJob\\" + path)
        first_node = int(file.readline().rstrip())
        tree = NodeABB(first_node)
        
        for line in file:
            node = NodeABB(int(line.rstrip()))
            tree.add(node)
        print("Árvore criada com sucesso.")
        file.close()

        return tree

    def clean_terminal():
        os.system("pause")
        clear()

    def menu_options():
        
        option = 0

        while(option != 4):
            print(f'================================')
            print(f'Informe umas das opções abaixo: ')
            print(f'1 - Abrir Arquivo')
            print(f'2 - Mostrar Árvore')
            print(f'3 - Mostrar os Percursos')
            print(f'4 - Encerrar o Programa')
            option = int(input('Resposta: '))
            print(f'================================')

            if option == 1:
                clear()
                print(f'========== Abrindo arquivo para montar árvore ==========')
                print(f'Criar arquivo (.txt) na pasta treeBinarySearchJob!')
                path = input('Nome do arquivo (txt): ')
                tree = open_file(path)
                print(f'\n')
                clean_terminal()
            elif option == 2:
                clear()
                print(f'========== Apresentando árvore binária ==========')
                view_tree(tree)
                print(f'\n')
                clean_terminal()
            elif option == 3:
                clear()
                print(f'========== Apresentando os percursos ==========')
                view_routes(tree)
                print(f'\n')
                clean_terminal()
            elif option == 4:
                clear()
                tree = None
                print(f'Encerrando programa...')
                clean_terminal()
                break

    menu_options()