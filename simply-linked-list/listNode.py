
class ListNode:
    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data
    
    def setData(self, _data):
        self.data = _data

    def getNextNode(self):
        return self.nextNode
    
    def setNextNode(self, _nextNode):
        self.nextNode = _nextNode