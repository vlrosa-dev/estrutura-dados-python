
from doublyLinkedList import DoublyLinkedListIterator

if __name__ == '__main__':

    list = DoublyLinkedListIterator()

    '''
    Adding multiple values - addNode()
    '''
    list.addNode(10)
    list.addNode(20)
    list.addNode(30)
    print(f'method addNode(): ', end='')
    list.printNode() # [ 10 20 30 ]

    '''
    Adding multiple values - insNode()
    '''
    list.insNode(40)
    list.insNode(50)
    list.insNode(60)
    print(f'method insNode(): ', end='')
    list.printNode() # [ 60 50 40 ]

    '''
    Operation in the TAD List
    '''    
    print(f'process method elimNode(): ', end='')
    list.elimNode() 
    list.printNode()

    print(f'process method posNode(): ', end='')
    list.posNode(2)
    print(f'move position at data = {list.iterator.data}')

    print(f'process method elimNode(): ', end='')
    list.elimNode()
    list.printNode()