
from simplyLinkedList import SimplyLinkedList

if __name__ == '__main__':
    
    '''01 Verificar se a lista estão iguais
        Condições: 
        - Se ambas as estruturas tem o mesmo número de elementos, e são iguais um por um
        - Duas listas vazias são iguais
    '''
    def equalsLists(lst1, lst2):
        if lst1.size != lst2.size:
            return False
        else:
            nodeLst1 = lst1.first_Node() 
            nodeLst2 = lst2.first_Node()
            while nodeLst1:
                if(nodeLst1.data != nodeLst2.data):
                    return False
                else:
                    nodeLst1 = nodeLst1.nextNode()
                    nodeLst2 = nodeLst2.nextNode()
            return True

    '''02 Verificar se as listas são semelhantes
        Condições:
        - São semelhantes se têm os mesmos elementos, mesmo em ordem diferente
        - Se está repetido em uma lista, deve aparecer na outra lista
    '''
    def similarLists(lst1, lst2):
        if lst1.size == 0: # Verifica se lista1 está vazia
            return False
        elif lst2.size == 0: 
            return False
        elif lst1.size != lst2.size:
            return False
        else:
            cont = 0
            lst1.first_Node()
            while not lst1.isUndefinedIterator():
                data1 = lst1.iterator.data
                lst2.first_Node()
                while not lst2.isUndefinedIterator():
                    data2 = lst2.iterator.data
                    if data1 == data2:
                        cont += 1
                    lst2.nextNode()
                lst1.nextNode()
            if lst1.size == cont:
                return True
            else:
                return False
    
    '''03 Verificar se a lista lst2 é uma sublista de lst1'''
    def subList(lst1, lst2):
        pass

    '''05 Verificar se a lista esta ordenada de forma crescente'''
    def verifyListOrderAscending(lst):
        if lst.size == 0:
            return False
        elif lst.size == 1:
            return True
        else:
            lst.first_Node()
            while not lst.iterator.nextNode:
                if(lst.iterator.data > lst.iterator.nextNode.data):
                    return False
                lst.nextNode()
            return True

    '''06 Adicionar elemento ao fim da lista'''
    def addingList(lst1, data):
        lst1.last_Node()
        lst1.addingNode(data)

    '''07 Substituir conteúdo atual do iterador pelo elemento'''
    def substituteIteratorData(lst, data):
        if lst.size == 0:
            return False
        else:
            lst.iterator.data = data

    '''08 Indicar se o elemento existe na lista'''
    def verifyDataInList(lst, data):
        if lst.size == 0:
            return False
        else:
            lst.first_Node() 
            while not lst.isUndefinedIterator():
                if lst.iterator.data == data:
                    return True
                lst.nextNode()
            return False

    '''09 Exibe todos os elementos da lista, utilizando a operação posLista para avançar'''
    def viewList(lst):
        if lst.size == 0:
            print('Lista Vazia!')
        else:
            i = 1
            while i <= lst.size:
                lst.moveNode(i)
                print(lst.iterator.data)
                i += 1

    '''10 Coloca o iterador na posição anterior à atual'''
    def setIteratorPositionPrevious(lst):
        if lst.size == 0:
            return False
        elif lst.firstNode == lst.lastNode:
            return False
        else:
            currentIterator = lst.firstNode
            while currentIterator.nextNode != lst.iterator:
                currentIterator = currentIterator.nextNode
            lst.iterator = currentIterator

    '''11 Retorna a posição do iterador na lista'''
    def returnPositionIterator(lst):
        if lst.size == 0:
            print('Lista vazia!')
        else:
            cont = 0
            currentIterator = lst.firstNode
            while currentIterator != lst.iterator:
                cont += 1
                currentIterator = currentIterator.nextNode
            cont += 1
        return cont

    '''19 Elimina da lista lst1 todos os elementos que aparecem na lista lst2'''
    def differenceList(lst1, lst2):
        pass

    # Instanciando objeto Lista
    simplyLinkedList = SimplyLinkedList()

    # Adicionando elementos na lista 1
    simplyLinkedList.addingNode(1)
    simplyLinkedList.addingNode(2)
    simplyLinkedList.addingNode(3)