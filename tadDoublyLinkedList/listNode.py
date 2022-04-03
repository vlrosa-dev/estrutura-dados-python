'''
    Desenvolvido por:
        - Lucas Azevedo Zortea
        - Marcelo Dalvi
        - Rhayane Couto Fabres
        - Victor Luis Moreira Rosa
'''

class ListNode:
    def __init__(self, data, nextNode = None, antNode = None):
        self.data = data
        self.nextNode = nextNode
        self.antNode = antNode

    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, val):
        self.nextNode = val

    def getAntNode(self):
        return self.antNode

    def setAntNode(self, val):
        self.antNode = val