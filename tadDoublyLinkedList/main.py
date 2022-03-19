
from doublyLinkedList import DoublyLinkedListIterator

if __name__ == '__main__':

    list = DoublyLinkedListIterator()

    '''Adicionando Valores!'''
    list.addNode(10)
    list.addNode(20)
    list.addNode(30)
    list.insNode(40)
    print(f'Adicionando Valores')
    list.printNode()

    print('Depois da tratativa')
    list.posNode(1)
    list.elimNode()
    list.printNode()