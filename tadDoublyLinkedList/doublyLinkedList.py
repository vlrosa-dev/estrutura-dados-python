
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

    def undefinedIterator(self):
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
            self.firstNode = newNode
            self.lastNode = newNode
            self.iterator = newNode

        elif self.iterator == self.lastNode:
            newNode.nextNode = None
            newNode.antNode = self.iterator
            self.iterator.nextNode = newNode
            self.lastNode = newNode
            self.iterator = newNode

        else:
            newNode.antNode = self.iterator
            newNode.nextNode = self.iterator.nextNode
            self.iterator.nextNode = newNode
            self.iterator = newNode

        self.size += 1
        return True      

    def insNode(self, data):
        newNode = ListNode(data, None, None)
        if self.size == 0:
            self.firstNode = newNode
            self.lastNode = newNode
            self.iterator = newNode
        
        elif self.iterator ==  self.firstNode:
            newNode.nextNode = self.iterator
            self.iterator.antNode = newNode
            self.iterator = newNode
        
        else:
            newNode.nextNode = self.iterator
            newNode.antNode = self.iterator.antNode
            self.iterator.antNode.nextNode = newNode
            self.iterator.antNode = newNode
            self.iterator = newNode

    def elimNode(self):
        if self.iterator == self.lastNode:
            if self.firstNode == self.lastNode:
                self.firstNode = None
                self.lastNode = None
                self.iterator = None
            else:
                self.iterator.antNode.nextNode = None
                self.iterator = self.iterator.antNode
        else:
            if self.iterator == self.lastNode:
                self.iterator.antNode.nextNode = None
                self.iterator = self.iterator.antNode
            else:
                self.iterator.antNode.nextNode = self.iterator.nextNode
                self.iterator.nextNode.antNode = self.iterator
                self.iterator = self.iterator.nextNode

    def posNode(self, position):
        if position >= 1 and position <= self.size:
            i = 1
            self.iterator = self.firstNode
            while i < position:
                if self.iterator.nextNode != None:
                    self.iterator = self.iterator.nextNode
                    i += 1
            return True
        else:
            return False