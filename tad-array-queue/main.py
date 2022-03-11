from arrayQueue import ArrayQueue

if __name__ == "__main__":
  
  def printQueue(q):
    copia = ArrayQueue()  # instaciou fila auxiliar
    print('[', end="")
    
    while(not q.is_empty()): # enquanto a fila q nao ficar vazia
      print(q.first(), end=" ") # exibe o elemento que esta como primeiro da fila
      copia.enqueue(q.dequeue()) # adicionar o elem da frente na fila auxiliar e desenfileirar
    
    while(not copia.is_empty()):
      q.enqueue(copia.dequeue())
      
    copia = None
    print(']\n')

  def printArray(lista):
    lista.first_Node() # por o iterador sobre o primeiro elemento
    while not lista.isUndefinedIterator():
      print(lista.get_iterator().getData(), end=" ")
      lista.nextNode() # avanca iterador para proximo noh
    
    print('\n')

  """01 - Insere o elemento na fila dada uma posição"""
  def insertElementInPosition(array, element, position):
    copy = ArrayQueue
    aux = 0
    if len(array) == 0 and position == 0: """Fila Vazia"""
      array.enqueue(element)
    elif (position > 0 and position < len(array) + 1): """Posição Válida"""
      while (not array.is_empty()):
        if aux == position: 
          copy.enqueue(element)
          aux += 1
        else:
          copy.enqueue(array.dequeue)
          aux +=1
      while (not copy.is_empty()):
        array.enqueue(copy.dequeue())       
    else:
      print('Invalid Position!')

  """02 - Concatenar filas"""
  def concatQueue(array f1, array f2):
    copia = ArrayQueue
    copia = ArrayQueue(f2)
    
    while (not f2.is_empty()):
      f1.enqueue(f2.dequeue())
    while (not copia.is_empty()):
      f2.enqueue(copia.dequeue())
    copia = None

  """03 - Coloca o elemento na primeira posição da fila"""
  def firstQueue(array, element):
    copia = ArrayQueue()
    copia.enqueue(element)
    
    while (not array.is_empty):
      copia.enqueue(array.dequeue())
    while (not copia.is_empty):
      array.enqueue(copia.dequeue())
    copia = None

  """04 - Verifica se o elemento existe na fila"""
  def searchElement(array, element):
    if array.is_empty:
      return False
    else:
      while (not array.is_empty):
        if (array.dequeue() == element):
          return True
      return False
  
  array = ArrayQueue()
  array.enqueue(5)
  array.enqueue(10)
  array.enqueue(20)
  array.dequeue()
  printQueue(array)