
from simplyLinkedList import SimplyLinkedList

if __name__ == '__main__':
    
    # Instanciando objeto Lista!
    simplyLinkedList = SimplyLinkedList()

    # Adicionando elementos na lista!
    simplyLinkedList.addingNode(10)
    simplyLinkedList.addingNode(20)
    simplyLinkedList.addingNode(30)
    print("Método addingNode()")
    simplyLinkedList.printNode()

    # Inserindo Elementos na lista!
    simplyLinkedList.insertNode(40)
    simplyLinkedList.insertNode(50)
    print("Método insertNode()")
    simplyLinkedList.printNode()

    # Movendo o iterador!
    simplyLinkedList.moveNode(3)

    # Removendo elementos da lista!
    simplyLinkedList.removeNode()

    print("Lista Final!")
    simplyLinkedList.printNode()