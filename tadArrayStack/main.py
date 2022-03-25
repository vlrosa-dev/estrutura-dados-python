
from tadArrayQueue.arrayQueue import ArrayQueue
from tadSimplyLinkedList.simplyLinkedList import SimplyLinkedList
from arrayStack import ArrayStack

if __name__ == '__main__':

  def printStack(stack):
    copia = ArrayStack()
    print('[', end="")

    while (not stack.is_empty()):
      print(stack.top(), end=" ")
      copia.push(stack.pop())
    
    while (not copia.is_empty()):
        stack.push(copia.pop())
    print(']\n')
    copia = None

  def copyStackArray(stack):
    copia = ArrayStack()
    apoio = ArrayStack()

    while (not stack.is_empty()):
      apoio.push(stack.pop())

    while (not apoio.is_empty()):
      copia.push(apoio.pop())
      stack.push(apoio.pop())

    apoio = None
    return copia

  def copyStackArrayWithSimplyLinkedList(stack):
    copia = ArrayStack()
    apoio = SimplyLinkedList()

    while (not stack.is_empty()):
      apoio.insertNode(stack.pop())

    while (not apoio.isUndefinedIterator()):
      stack.push(apoio.data)
      copia.push(apoio.data)
      apoio.removeNode()

    apoio = None
    return copia

  def verifyPalindromeStack(stack):
    copyQueue = ArrayQueue()
    copyStack = ArrayStack()

    while not stack.is_empty():
      varStack = stack.pop()
      copyQueue.enqueue(varStack)
      copyStack.push(varStack)

    while not stack.is_empty():
      if copyQueue.dequeue() != copyStack.pop():
        print(f'Não é um palindromo')
        return False
    
    print(f'É um palindromo')
    return True

  def removeAllOcorrencyElementStack(stack, elem):
    copyStack = ArrayStack()

    while not stack.is_empty():
      varStack = stack.pop()
      if varStack != elem:
        copyStack.push(varStack)

    while not copyStack.is_empty():
      stack.push(stack.pop())

    return True

  stack = ArrayStack()
  stack.push(10)
  stack.push(20)
  stack.push(10)
  printStack(stack)