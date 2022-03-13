from arrayQueue import ArrayQueue

if __name__ == "__main__":
  
  def printQueue(lst):
    copia = ArrayQueue()
    print('[', end="")
    while(not lst.is_empty()):
      print(lst.first(), end=" ")
      copia.enqueue(lst.dequeue())
    while(not copia.is_empty()):
      lst.enqueue(copia.dequeue())  
    copia = None
    print(']\n')

  def printArray(lst):
    lst.first_Node()
    while not lst.isUndefinedIterator():
      print(lst.get_iterator().getData(), end=" ")
      lst.nextNode()
    print('\n')

  """01 Insere o elemento na fila dada uma posição"""
  def insertElementInPosition(lst, element, position):
    copy = ArrayQueue()
    aux = 0
    if len(lst) == 0 and position == 0:
      lst.enqueue(element)
    elif (position > 0 and position < len(lst) + 1):
      while (not array.is_empty()):
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

  """02 Concatenar filas"""
  def concatQueue(lst1, lst2):
    copia = ArrayQueue
    copia = ArrayQueue(lst2)
    while (not lst2.is_empty()):
      lst1.enqueue(lst2.dequeue())
    while (not copia.is_empty()):
      lst2.enqueue(copia.dequeue())
    copia = None

  """03 Posiciona o elemento na primeira posição da fila"""
  def firstQueue(array, element):
    copia = ArrayQueue()
    copia.enqueue(element)
    
    while (not array.is_empty):
      copia.enqueue(array.dequeue())
    while (not copia.is_empty):
      array.enqueue(copia.dequeue())
    copia = None

  """04 Verifica se o elemento existe na fila"""
  def searchElement(array, element):
    if array.is_empty:
      return False
    else:
      while (not array.is_empty):
        if (array.dequeue() == element):
          return True
      return False
  
  queue = ArrayQueue()
  queue.enqueue(5)
  queue.enqueue(10)
  queue.enqueue(20)
  queue.dequeue()
  printQueue(queue)