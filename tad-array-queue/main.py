
from arrayQueue import ArrayQueue

if __name__ == "__main__":

    def printFila(q):
        copia = ArrayQueue()  # instaciou fila auxiliar
        print('[', end="")
        while(not q.is_empty()): # enquanto a fila q nao ficar vazia
            print(q.first(), end=" ") # exibe o elemento que esta como primeiro da fila
            copia.enqueue(q.dequeue()) # adicionar o elem da frente na fila auxiliar e desenfileirar
        while(not copia.is_empty()):
            q.enqueue(copia.dequeue())
        copia = None
        print(']\n')

    """1) Fila copiarFila( Fila f ) 
Fazer uma cópia de uma Fila, usando como apoio uma lista. Também é 
possível usar como apoio uma fila. A Fila original deve ser restaurada."""

    def copiarFila(f):
        copia = ArrayQueue() # copia a ser retornada
        copiaRestaura = ArrayQueue() # copia para restaurar a fila f
        while(not f.is_empty()):
            elem = f.dequeue()
            copia.enqueue(elem)
            copiaRestaura.enqueue(elem)
        while(not copiaRestaura.is_empty()):
            f.enqueue(copiaRestaura.dequeue())
        copiaRestaura = None
        return copia

    def copiarFilaUsandoLista(f):
        copia = ArrayQueue() # copia a ser retornada
        lst = SinglyLinkedListIterator() # copia para restaurar a fila f
        while(not f.is_empty()):
            elem = f.dequeue()
            copia.enqueue(elem)
            lst.addNode(elem)
        lst.first_Node() # iterador no primeiro elemento da lista
        while(not iterator):
            f.enqueue(lst.get_iterator().getData()) # lst.iterator.data
            lst.elim_Node()
        lst = None
        return copia

    """3) void concatFilas(Fila f1, Fila f2) 
Concatenar duas filas, deixando o resultado na primeira(f1). A fila f2 deve 
ser restaurada. Sugestão: usar como apoio outra fila."""

    def concatFilas(f1, f2):
        copia = ArrayQueue() # copia da fila f2 para restauracao
        copia = copiarFila(f2)
        while(not f2.is_empty()): # enquanto a fila f2 nao ficar vazia
            f1.enqueue(f2.dequeue()) # adiciona o primElem de f2 no fim de f1
        while(not copia.is_empty()):
            f2.enqueue(copia.dequeue())
        copia = None


    """10) primeiroDaFila( Fila f, TipoF elem) 
Coloca o elemento elem na primeira posição da fila. """
    def primeiroDaFila(fila, elem):
        filaApoio = ArrayQueue() # crio uma nova fila para guardar
        filaApoio.enqueue(elem) # insiro elem na fila
        while(not fila.is_empty()):
            filaApoio.enqueue(fila.dequeue())
        while(not filaApoio.is_empty()):
            fila.enqueue(filaApoio.dequeue())
        filaApoio = None


    # adicionar o elmento elem numa posicao pos dada.
    def adicionaNaPosicaoPos(fila, elem, posicao):
        if(len(fila) == 0 and posicao == 0): # filza vazia
            fila.enqueue(elem)
        elif( posicao >=0 and posicao <= len(fila)+1):
            contaPosicao = 0
            filaApoio = ArrayQueue()
            while(not fila.is_empty()):
                if(contaPosicao == posicao): # eh a posicao a ser inserida
                    filaApoio.enqueue(elem)
                    contaPosicao += 1
                else:
                    contaPosicao += 1
                    filaApoio.enqueue(fila.dequeue())
            while(filaApoio):
                fila.enqueue(filaApoio.dequeue())
        else:
            print('posicao invalida')

    """5) int existeElemento( Fila f, TipoF elem) 
Retorna true(1) se o elemento elem está presente na fila e false(0) caso 
contrário. """

    def existeElemento(fila, elem):
        if( fila.is_empty()): # fila vazia
            return False
        else:
            copia = copiarFila(fila)
            while(copia): # enquanto tiver elemento
                if(elem == copia.dequeue()):
                    copia = None # ajudar garbage collector
                    return True
            copia = None
            return False




    def printLista(lista):
        lista.first_Node() # por o iterador sobre o primeiro elemento
        while not lista.isUndefinedIterator():
            print(lista.get_iterator().getData(), end=" ")
            lista.nextNode() # avanca iterador para proximo noh
        print('\n')

    Q = ArrayQueue() # cria uma fila vazia
    Q.enqueue(5) # adiciona no fim da fila o 5
    printFila(Q) # [5 ]
    Q.enqueue(3) # adiciona no fim da fila o 3
    printFila(Q) # [5 3 ]
    print('tamanho da fila = {}'.format(len(Q))) # tamanho da fila = 2
    Q.dequeue() # remove e retorna o primeiro elemento da fila: 5
    printFila(Q) # [3 ]
    if(Q.is_empty()): # verifica se a fila esta vazia
        print('fila vazia')
    else:
        print('fila cheia')
    Q.dequeue() # remove e retorna o primeiro elemento da fila: 3
    printFila(Q)  # [ ]
    if (Q.is_empty()):
        print('fila vazia')
    else:
        print('fila cheia')
    Q.dequeue() # remove e retorna o primeiro elemento da fila: mas já está vazia: fila vazia
    Q.enqueue(7) # [7 ] # adiciona no fim da fila o 7
    printFila(Q)
    Q.enqueue(9)  # [7 9 ] # adiciona no fim da fila o 9
    printFila(Q)  # retorna o primeiro elemento da fila sem remover : 7
    print('primeiro elem da fila = {}'.format(Q.first()))

    fila2 = ArrayQueue() # criando nova fila
    fila2= copiarFila(Q) # criando uma copia da fila Q
    printFila(fila2)
    concatFilas(fila2,Q)
    printFila((fila2))
    printFila(Q)

    primeiroDaFila(fila2, 100)
    printFila(fila2)

    adicionaNaPosicaoPos(fila2, 200, 3)
    printFila(fila2)

    if (existeElemento(fila2,200)):
        print('existe 200')
    else:
        print('nao existe 200')

    # for i in range(8):
    #     Q.enqueue(i*10)
    #     print('i={} size={}'.format(i,len(Q)))
    #     printFila(Q)
    #
    # Q.dequeue()
    # Q.enqueue(80)
    # printFila(Q)

    # lst = SinglyLinkedListIterator()
    # for i in range(5):
    #     lst.addNode(i)
    # printLista(lst)