
class ArrayQueue:
    """
    FIFO queue implementation using a Python list as underlying storage.
    """
    DEFAULT_CAPACITY = 10     

    def __init__(self):
      """
      Create an empty queue.
      """
      self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
      self._size = 0
      self._first = -1
      self._last = -1

    def __len__(self):
      """
      Return the number of elements in the queue.
      """
      return self._size

    def is_empty(self):
      """
      Return True if the queue is empty.
      """
      return self._size == 0

    def first(self):
      """
      return the first element in queue
      """
      if self.is_empty():
        print('Queue is empty!')
        return None
      else:
        return self._data[self._first]

    def dequeue(self):
      """
      remove and return the first element in queue
      """
      if self.is_empty():
        print('Queue is empty!')
        return None
      else:
        answer = self._data[self._first]
        self._data[self._first] = None      
        if(self._first == self._last):
          self._first = -1
          self._last = -1
        else:
            self._first = (self._first + 1) % len(self._data)
          
        self._size -= 1
        return answer

    def enqueue(self, e):
      """
      insert data the last position in queue
      """
      if self._size == len(self._data):
        self._resize(2 * len(self.data))   
      if(self._size == 0):
        self._data[0] = e
        self._first = 0
        self._last = 0
      else:
        self._last = (self._last + 1) % len(self._data)
        self._data[self._last] = e  
      self._size += 1

    def _resize(self, cap):
      """
      Realocate the length in queue
      """
      old = self._data
      self._data = [None] * cap
      walk = self._first
      for k in range(self._size):
        self._data[k] = old[walk]
        walk = (1 + walk) % len(old)        
      self._first = 0          