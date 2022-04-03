from arrayQueue import ArrayQueue

if __name__ == "__main__":
  
    def printWithQueue(lst):
      copia = ArrayQueue()
      print('[', end="")
      while(not lst.is_empty()):
        print(lst.first(), end=" ")
        copia.enqueue(lst.dequeue())
      while(not copia.is_empty()):
        lst.enqueue(copia.dequeue())  
      copia = None
      print(']\n')

    def printWithArray(lst):
      lst.first_Node()
      while not lst.isUndefinedIterator():
        print(lst.get_iterator().getData(), end=" ")
        lst.nextNode()
      print('\n')

    def insertElementInPositionSpecific(lst, element, position):
      copy = ArrayQueue()
      aux = 0
      if len(lst) == 0 and position == 0:
        lst.enqueue(element)
      elif (position > 0 and position < len(lst) + 1):
        while (not lst.is_empty()):
          if aux == position: 
            copy.enqueue(element)
            aux += 1
          else:
            copy.enqueue(lst.dequeue)
            aux +=1
        while (not copy.is_empty()):
          lst.enqueue(copy.dequeue())       
      else:
        print('Invalid Position!')

    def concatenateQueues(lst1, lst2):
      copia = lst2
      while (not lst2.is_empty()):
        lst1.enqueue(lst2.dequeue())
      while (not copia.is_empty()):
        lst2.enqueue(copia.dequeue())
      copia = None

    def placeElementInFirstPosition(array, element):
      copia = ArrayQueue()
      copia.enqueue(element)
      
      while (not array.is_empty):
        copia.enqueue(array.dequeue())
          
      while (not copia.is_empty):
        array.enqueue(copia.dequeue())
      copia = None

    def searchElementInQueue(array, element):
      if array.is_empty:
        return False
      else:
        while (not array.is_empty):
          if (array.dequeue() == element):
            return True
        return False

    def removeElementInQueue(fila, elem):
      filaApoio = ArrayQueue()
      
      while not fila.is_empty():
        data = fila.dequeue()
        if data != elem:
          filaApoio.enqueue(data)
              
      while not filaApoio.is_empty():
        fila.enqueue(filaApoio.dequeue())
      return True