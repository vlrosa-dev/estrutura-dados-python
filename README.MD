# Disciplina Estrutura de Dados
    Segue abaixo as estruturas apresentadas dentro da disciplina.
## TAD Lista Simplesmente Encadeada (SimplyLinkedList)
    Esse tipo de lista se apresenta de maneira encadeada, um ao lado do outro e seu nó só possui
    referência para o próximo nó.
    
    Segue estrutura do node(nó):
    - elemento(informação que será inserida no nó)
    - nextNode(referência ao próximo nó da lista)

    Segue estrutura básica da Lista(SimplyLinkedList):
    - iterator(posiciona sob o nó da lista)
    - addNode(adiciona um nó ao final da lista e coloca o iterador sobre o mesmo)
    - elimNode(remove o nó sob o iterador e coloca sobre o próximo)
    - insNode(insere um nó antes do iterador e coloca o iterador sobre ele)
    - posNode(posiciona o iterador com base em uma posição da lista)
    - first_Node(coloca o iterador sobre o primeiro nó)
    - next_Node(avança o iterador para o próximo nó)
    - isUndefinedIterator(verifica se o iterador está indefinido)

## TAD Lista Duplamente Encadeada (DoublyLinkedList)
    Esse tipo de lista se apresenta de maneira encadeada, mas um pouco diferente 
    da primeira apresentada, o seu nó faz referência para o próximo nó e nó anterior.

    Segue estrutura do node(nó):
    - elemento(informação que será inserida no nó)
    - nextNode(referência ao próximo nó da lista)
    - antNode(referência para o nó anterior da lista)

    Segue estrutura básica da Lista (DoublyLinkedList):
    - iterator(posiciona sob o nó da lista)
    - addNode(adiciona um nó ao final da lista e coloca o iterador sobre o mesmo)
    - elimNode(remove o nó sob o iterador e coloca sobre o próximo)
    - insNode(insere um nó antes do iterador e coloca o iterador sobre ele)
    - posNode(posiciona o iterador com base em uma posição da lista)
    - first_Node(coloca o iterador sobre o primeiro nó)
    - next_Node(avança o iterador para o próximo nó)
    - isUndefinedIterator(verifica se o iterador está indefinido)

## TAD Fila (Queue)
    Possui o mesmo conceito de uma fila, enfileira os elementos no conceito FIFO.

    Segue estrutura básica da fila(Queue):
    - isEmpty(verifica se a fila está vazia)
    - enqueue(enfileira o elemento ao fim da fila)
    - dequeue(retorna e remove o elemento do inicio da fila (FIFO))
    - resize(redimensiona o tamanho da fila)
    - first(retorna o primeiro elemento da fila)

## TAD Pilha (Stack)
    Possui o mesmo conceito de uma pilha (empilhar elementos), é do tipo LIFO.

    Segue estrutura básica da pilha(Stack):
    - top(retorna o elemento do topo da pilha)
    - pop(retorna e remove o elemento do topo da pilha)
    - push(adiciona o elemento no topo da pilha)
    - is_Empty(verifica se a pilha está vazia)