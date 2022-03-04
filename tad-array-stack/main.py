
from simplyLinkedList import SimplyLinkedList
from arrayStack import ArrayStack

if __name__ == '__main__':

  def printStack(s):
    copia = ArrayStack()
    
    print('[', end="")
    while(not s.is_empty()):
      print(s.top(), end=" ")
      copia.push(s.pop())
    
    while(not copia.is_empty()):
        s.push(copia.pop())
    print(']\n')
    copia = None

  def copyStackArray(self, array):
    copia = ArrayStack()
    apoio = ArrayStack()

    while (not array.is_empty()):
      apoio.push(array.pop())

    while (not apoio.is_empty()):
      copia.push(apoio.pop())
      array.push(apoio.pop())

    apoio = None

    return copia

  def copyStackArrayWithSimplyLinkedList(self, array):
    copia = ArrayStack()
    apoio = SimplyLinkedList()

    while (not array.is_empty()):
      apoio.insertNode(array.pop())

    while (not apoio.isUndefinedIterator()):
      array.push(apoio.data)
      copia.push(apoio.data)
      apoio.removeNode()

    apoio = None
    
    return Copia