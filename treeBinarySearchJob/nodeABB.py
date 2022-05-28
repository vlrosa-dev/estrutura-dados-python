
class NodeABB:

    def __init__(self, data=None, esq=None, dir=None):
        self._data = data
        self._esq = esq
        self._dir = dir

        if self._data:
            self._size = 1
        else:
            self._size = 0

    def setRaizArbin(self, elem):
        self._data = elem

    def raizArbin(self):
        return self._data

    def setDirArbin(self, arbin):
        self._dir = arbin

    def dirArbin(self):
        return self._dir

    def setEsqArbin(self, arbin):
        self._esq = arbin

    def esqArbin(self):
        return self._esq

    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def add(self, node):
        if node._data < self._data:
            if self._esq is None:
                self._esq = node
            else:
                self._esq.add(node)
        elif node._data > self._data:
            if self._dir is None:
                self._dir = node
            else:
                self._dir.add(node)
        self._size += 1

    def min(self):
        """Retorna o menor elemento da subárvore que tem self como raiz."""
        if self._esq is None:
            return self
        else:
            return self._esq.min()

    def removeMin(self):
        """Remove o menor elemento da subárvore que tem self como raiz."""
        if self._esq is None:
            return self._dir
        self._esq = self._esq.removeMin()
        return self

    def remove(self, elem):
        if elem < self._data:
            self._esq = self._esq.remove(elem)
        elif elem > self._data:
            self._dir = self._dir.remove(elem)
        else:
            if self._dir is None:
                return self._esq
            if self._esq is None:
                return self._dir
            tmp = self._dir.min()
            self._data = tmp._data
            self._dir.removeMin()
        return self
            