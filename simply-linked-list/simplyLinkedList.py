
from listNode import ListNode

class SimplyLinkedList:
    def __init__(self, _firstNode = None):
        self.firstNode = _firstNode
        self.lastNode = _firstNode
        self.iterator = _firstNode

        if self.firstNode:
            self.size = 1
        else:
            self.size = 0

    def firstNode(self):
        self.iterator = self.firstNode

    def lastNode(self):
        self.iterator = self.lastNode

    def nextNode(self):
        if self.iterator:
            self.iterator = self.iterator.ListNode.getNextNode()
            return True

    def isUndefinedIterator(self): # Verifica se o iterador não está definido
        if self.iterator == None:
            return True
        else:
            return False
    
    def printNode(self): # Imprime os valores da lista
        currentNode = self.firstNode

        while currentNode:
            print(f'{currentNode.data}')
            currentNode = currentNode.nextNode

    def addingNode(self, data):
        newNode = ListNode(data, None)
        if self.size == 0: # Valida se a lista está vazia
            self.firstNode = newNode
            self.lastNode = newNode
            self.iterator = newNode

        elif self.iterator == self.lastNode: # Iterador sobre último elemento
            self.lastNode.nextNode = newNode
            self.iterator = newNode
            self.lastNode = newNode

        else: # Iterador está sobre o elemente mais interno da lista
            newNode.nextNode = self.iterator.nextNode
            self.iterator.nextNode = newNode
            self.lastNode = newNode
        
        self.size += 1
        return True

    def insertNode(self, data):
        newNode = ListNode(data, None)
        if self.size == 0: # Tratamento caso a lista esteja vazia
            self.firstNode = newNode
            self.lastNode = newNode
            self.iterator = newNode
        
        elif self.iterator == self.firstNode: # Iterador esteja sobre o primeiro elemento
            newNode.nextNode = self.firstNode
            self.iterator = newNode
            self.firstNode = newNode

        else: # Iterador está sobre um elemento mais interno da lista
            currentNode = self.firstNode
            while currentNode.nextNode != self.iterator:
                currentNode = currentNode.nextNode
            
            currentNode.nextNode = newNode
            newNode.nextNode = self.iterator
            self.iterator = newNode
        
        self.size += 1
        return True

    def removeNode(self):
        if self.iterator == self.firstNode: # Verifica se iterador está sobre o primeiro elemento
            if self.firstNode == self.lastNode: # Verifica se existe apenas um node
                self.firstNode = None
                self.lastNode = None
                self.iterator = None
            else:
                self.firstNode = self.firstNode.nextNode # Verifica se tem mais de um node
                self.iterator.nextNode = None
                self.iterator = self.firstNode
        else: # O iterador está sobre o ultimo elemento ou internamente
            currentNode = self.firstNode
            while currentNode.nextNode != self.iterator:
                currentNode = currentNode.nextNode

            if self.iterator == self.lastNode: # Verifica se é o ultimo elemento
                self.iterator.nextNode = None
                self.iterator = currentNode
                self.lastNode = currentNode
                currentNode.nextNode = None
            else: # O iterador está no elemento mais interno da lista
                currentNode.nextNode = self.iterator.nextNode
                currentNode = self.iterator
                self.iterator = self.iterator.nextNode
                currentNode.nextNode = None
        
        self.size -= 1
        return True

    def moveNode(self, position):
        if (position > 0) and (position <= self.size): # Valida a posição inserida pelo usuário
            i = 1
            self.iterator = self.firstNode
            while i < position: # Percorre cada elemento através do nextNode
                if self.iterator.nextNode != None:
                    self.iterator = self.iterator.nextNode
                    i += 1
            return True
        else:
            return False