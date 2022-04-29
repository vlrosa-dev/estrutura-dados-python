
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

    def vaziaArbin(self):
        return len(self)==0

    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def add(self, node):  # caso da Arv vazia esta sendo tratada no construtor
        if node._data < self._data:  # data < raiz : inserir na subArvore esquerda
            if self._esq is None:  # subArvEsq eh vazia
                self._esq = node
            else:
                self._esq.add(node)
        elif node._data > self._data:  # data > raiz : inserir na subArv direita
            if self._dir is None:
                self._dir = node
            else:
                self._dir.add(node)
        self._size += 1

    def min(self):
        """Retorna o menor elemento da subárvore que tem self como raiz.
        """
        if self._esq is None:
            return self
        else:
            return self._esq.min()

    def removeMin(self):
        """Remove o menor elemento da subárvore que tem self como raiz.
        """
        if self._esq is None:  # encontrou o min, daí pode rearranjar
            return self._dir
        self._esq = self._esq.removeMin()
        return self

    def remove(self, elem):
        if elem < self._data:
            self._esq = self._esq.remove(elem)
        elif elem > self._data:
            self._dir = self._dir.remove(elem)
        else:
            # encontramos o elemento, então vamos removê-lo!
            if self._dir is None:
                return self._esq
            if self._esq is None:
                return self._dir
            # ao invés de remover o nó, copiamos os valores do nó substituto
            tmp = self._dir.min()
            self._data = tmp._data
            self._dir.removeMin()
        return self