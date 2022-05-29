
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
        file = open("C:\\Users\Victo\dev\estrutura-dados-python\\treeBinarySearchJob\\" + path)
        first_node = int(file.readline().rstrip())
        tree = NodeABB(first_node)
        
        for line in file:
            node = NodeABB(int(line.rstrip()))
            tree.add(node)
        print("Árvore criada com sucesso.")
        file.close()

        return tree

    def menu_options():
        
        option = 0

        while(option != 4):
            print(f'================================')
            print(f'Escolha umas das opções abaixo: ')
            print(f'1 - Abrir Arquivo')
            print(f'2 - Mostrar Árvore')
            print(f'3 - Mostrar os percursos')
            print(f'4 - Encerrar o programa')
            option = int(input('Resposta: '))
            print(f'================================')

            if option == 1:
                print(f'Abrindo arquivo para montar árvore...')
                print(f'Criar arquivo (.txt) na pasta treeBinarySearchJob!')
                path = input('Nome do arquivo (txt): ')
                tree = open_file(path)
                print(f'\n')
            elif option == 2:
                print(f'Apresentando árvore binária...')
                view_tree(tree)
                print(f'\n')
            elif option == 3:
                print(f'Apresentando os percursos...')
                view_routes(tree)
                print(f'\n')
            elif option == 4:
                tree = None
                print(f'Encerrando programa!')
                break

    menu_options()