'''
    Desenvolvido por:
        - Lucas Azevedo Zortea
        - Marcelo Dalvi
        - Rhayane Couto Fabres
        - Victor Luis Moreira Rosa
'''

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
        '''
        Put the iterator under the first node
        '''
        self.iterator = self.firstNode

    def last_Node(self):
        '''
        Put the iterator under the last node
        '''
        self.iterator = self.lastNode

    def nextNode(self):
        '''
        Advances the iterator to the next node
        '''
        if self.iterator:
            self.iterator = self.iterator.nextNode

    def undefinedIterator(self):
        '''
        Checks if iterator is undefined
        '''
        if self.iterator == None:
            return True
        else:
            return False
    
    def printNode(self):
        '''
        Displays list items
        '''
        print(f'[ ', end='')
        currentNode = self.firstNode
        while currentNode:
            print(f'{currentNode.data}', end=' ')
            currentNode = currentNode.nextNode
        print(f']')

    def addNode(self, data):
        '''
        Insert a node after the iterator and goes under this node
        :param data: int, string...
        :return True or False
        '''
        newNode = ListNode(data, None, None)
        if self.size == 0:
            '''
            Check if it is the first node in the list
            '''
            self.firstNode = newNode
            self.lastNode = newNode
            self.iterator = newNode

        elif self.iterator == self.lastNode:
            '''
            Check if iterator is under last node
            '''
            newNode.nextNode = None
            newNode.antNode = self.iterator
            self.iterator.nextNode = newNode
            self.lastNode = newNode
            self.iterator = newNode

        else:
            '''
            Iterator is under an innermost element
            '''
            newNode.antNode = self.iterator
            newNode.nextNode = self.iterator.nextNode
            self.iterator.nextNode.antNode = newNode
            self.iterator.nextNode = newNode
            self.iterator = newNode

        self.size += 1
        return True      

    def insNode(self, data):
        '''
        Insert a node before the iterator and places the iterator over it
        :param data: int, string...
        :return True or False
        '''
        newNode = ListNode(data, None, None)
        if self.size == 0:
            '''
            Check if it is the first node in the list
            '''
            self.firstNode = newNode
            self.lastNode = newNode
            self.iterator = newNode
        
        elif self.iterator ==  self.firstNode:
            '''
            Checks if the interactor is under the first node
            '''
            newNode.nextNode = self.iterator
            self.iterator.antNode = newNode
            self.firstNode = newNode
            self.iterator = newNode
        
        else:
            '''
            Iterator is under an innermost element
            '''
            newNode.nextNode = self.iterator
            newNode.antNode = self.iterator.antNode
            self.iterator.antNode.nextNode = newNode
            self.iterator.antNode = newNode
            self.iterator = newNode

        self.size += 1
        return True

    def elimNode(self):
        '''
        Drop the node and place the iterator under the next node
        :param void
        :return True or False
        '''
        if self.size == 0:
            '''
            Check if list is empty
            '''
            print(f'list is empty!')
        else:
            if self.iterator == self.lastNode: # self.iterator == self.firstNode
                '''
                Checks if iterator is under last node
                '''
                if self.firstNode == self.lastNode:
                    '''
                    Check if iterator is under last node, but one element
                    '''
                    self.firstNode = None
                    self.lastNode = None
                    self.iterator = None
                else:
                    '''
                    Iterator is under last node, but has many elements
                    '''
                    self.iterator.antNode.nextNode = None
                    self.lastNode = self.iterator.antNode
                    self.iterator = self.iterator.antNode

            elif self.iterator == self.firstNode:
                '''
                Check if iterator is under first node
                '''
                self.iterator.nextNode.antNode = None
                self.firstNode = self.iterator.nextNode
                self.iterator = self.iterator.nextNode
                
            else:
                '''
                Iterator is under an innermost element
                '''
                self.iterator.antNode.nextNode = self.iterator.nextNode
                self.iterator.nextNode.antNode = self.iterator.antNode
                self.iterator = self.iterator.nextNode
        
            self.size -= 1
            return True

    def posNode(self, position):
        '''
        Put the iterator under the position received in parameter
        :param position: int
        :return True or False
        '''
        if self.size == 0:
            '''
            Check if list is empty
            '''
            print(f'List is empty!')
        else:
            if position >= 1 and position <= self.size:
                '''
                Check if parameter position is greater than or equal to 1 and position is less than or
                equal to size.
                '''
                i = 1
                self.iterator = self.firstNode
                while i < position:
                    if self.iterator.nextNode != None:
                        self.iterator = self.iterator.nextNode
                        i += 1
                return True
            else:
                return False