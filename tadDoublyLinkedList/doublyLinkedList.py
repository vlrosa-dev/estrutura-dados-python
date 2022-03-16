
from tadDoublyLinkedList import ListNode

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
        else
            return False

    def addNode(self, data):
        newNode = ListNode()
        if self.size == 0:
            self.firstNode = None
            self.lastNode = None
            self.iterator = None
        elif self.iterator = self.firstNode:

    def elimNode(self, data):
        pass

    def insNode(self, data):
        pass

    def posNode(self, position):
        pass