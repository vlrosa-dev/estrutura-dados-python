
from listNode import ListNode

class DoublyLinkedListIterator:
    def __init__(self, _firstNode = None):
        self.firstNode = _firstNode
        self.lastNode = _firstNode
        self.iterator = _firstNode

        if self.firstNode:
            self.size = 1
        else:
            self.size = 0

    def first_Node(self):
        self.iterator = self.firstNode

    def last_Node(self):
        self.iterator = self.lastNode

    def nextNode(self):
        if self.iterator:
            self.iterator = self.iterator.nextNode

    def isUndefinedIterator(self):
        if self.iterator == None:
            return True
        else:
            return False
    
    def printNode(self):
        currentNode = self.firstNode
        while currentNode:
            print(f'{currentNode.data}')
            currentNode = currentNode.nextNode

    def addNode(self, data):
        newNode = ListNode(data, None, None)
        if self.size == 0:
            self.firstNode = None
            self.lastNode = None
            self.iterator = None

        elif self.iterator == self.lastNode:
            newNode.nextNode = self.iterator
            self.firstNode = newNode
            self.iterator = newNode

        else:
            newNode.nextNode = self.iterator
            newNode.antNode = self.iterator.antNode
            self.iterator.antNode = newNode
            self.iterator.antNode.nextNode = newNode

        self.size += 1
        return True      

    def elimNode(self):
        if self.iterator == self.lastNode:
            if self.firstNode == self.lastNode:
                self.firstNode = None
                self.lastNode = None
                self.iterator = None
            else:
                self.firstNode = self.iterator.nextNode
                self.iterator.nextNode.antNode = None
                self.iterator = self.iterator.nextNode
        else:
            if self.iterator == self.lastNode:
                self.iterator.antNode.nextNode = None
            else:
                self.iterator.antNode.nextNode = self.iterator.nextNode
                self.iterator.nextNode.antNode = self.iterator

    def insNode(self, data):
        pass

    def posNode(self, position):
        pass