
class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10     

    def __init__(self):
      """Create an empty queue."""
      self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
      self._size = 0
      self._first = -1
      self._last = -1

    def __len__(self):
      """Return the number of elements in the queue."""
      return self._size

    def is_empty(self):
      """Return True if the queue is empty."""
      return self._size == 0

    def first(self): """Return first element in queue"""
      if self.is_empty():
        print('Queue is empty!')
        return None
      else:
        return self._data[self._first]

    def dequeue(self): """Remove and return the first element in queue""" 
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

    def enqueue(self, e): """Added element in the last position"""
      if self._size == len(self._data):
        self._resize(2 * len(self.data))     # double the array size
      if(self._size == 0):  # fila vazia
        self._data[0] = e
        self._first = 0 # o primeiro elemento esta na posicao zero
        self._last = 0  # o ultimo elemento esta na posicao zero
      else:
        self._last = (self._last + 1) % len(self._data) # determina a nova posicao do ultimo elemento
        self._data[self._last] = e  # adicona e como ultimo elemento na fila
      self._size += 1

    def _resize(self, cap): """Resize to a new list of capacity >= len(self)."""
      old = self._data                       # keep track of existing list
      self._data = [None] * cap              # allocate list with new capacity
      walk = self._first
      for k in range(self._size):            # only consider existing elements
        self._data[k] = old[walk]            # intentionally shift indices
        walk = (1 + walk) % len(old)         # use old size as modulus
      self._first = 0                        # front has been realigned