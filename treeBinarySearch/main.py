
from treeBinarySearch import NodeABB

if __name__ == '__main__':

    def preOrdemArbin(node:NodeABB):
        if node is not None:
            print(node._data) 
            if node._esq is not None:
                preOrdemArbin(node._esq)
            if node._dir is not None:
                preOrdemArbin(node._dir)

    def preOrdemArbin2(node:NodeABB):
        if node is not None:
            print(node.raizArbin())
            if node.esqArbin() is not None: 
                preOrdemArbin(node.esqArbin())
            if node.dirArbin() is not None:
                preOrdemArbin(node.dirArbin())

    """1) int pesoArbin( Arbin a){...} 
    Calcular e retornar o peso de uma árvore binária ( número de elementos da árvore). 
    Obs: a complexidade desta função é O(N) 
    """
    def pesoArbin(arbin:NodeABB):
        #arbin vazia retornar zero
        # ponto de parada
        if(arbin is None): # arbin.vaziaArbin()
            return 0
        else:
            return(1 + pesoArbin(arbin.esqArbin()) + pesoArbin(arbin.dirArbin()))
            #return(1 + pesoArbin(arbin._esq) + pesoArbin(arbin._dir))


    """2) int estaArbin( Arbin a, TipoA elem){...} 
    Verificar se um elemento está presente em uma árvore binária. 
    Obs: a complexidade desta função é O(N) se a árvore estiver degenerada e O(log N) se a 
    árvore estiver balanceada(cheia).
    """
    def estaArbin(arbin:NodeABB, elem):
        # se arbin vazia entao elem nao esta: retornar False
        # se elem == raiz, elem esta presente: retornar True
        # do contrario procurar elem na subArv esq e dir: Arv binaria
        # se for uma ABB ou ele esta na subArvEsq ou na SubArvDir
        # ponto de parada da arv vazia
        if(arbin is None):  #arbin.vaziaArbin()
            return False
        elif(arbin.raizArbin() == elem): #arbin._data == elem
            return True
        elif(elem < arbin.raizArbin()): #  elem < arbin._data : arbin eh um arv binaria de busca
            return estaArbin(arbin.esqArbin(), elem) #arbin._esq
        else: # elem > arbin.raizArbin()
            return estaArbin(arbin.dirArbin(), elem)
    
        # else: # se arbin for somente uma arvore binaria
        #     return(estaArbin(arbin.esqArbin()) or estaArbin(arbin.dirArbin()))


    # verifica se o elem esta presente na ABB arbin
    def insArbinBusca(arbin:NodeABB, elem):
        #arbin esta vazia
        if arbin is None:
            arbin = NodeABB(elem)
        elif(elem < arbin.raizArbin()): #elem menor que a raiz
            arbin._esq = insArbinBusca(arbin.esqArbin(), elem)
            #arbin.setEsqArbin(insArbinBusca(arbin.esqArbin(), elem))
        elif(elem > arbin.raizArbin()): #elem maior que a raiz
            arbin._dir = insArbinBusca(arbin.dirArbin(), elem)
            #arbin.setDirArbin(insArbinBusca(arbin.dirArbin(), elem))
        return arbin

    def altura(arbin:NodeABB):
        if arbin is None:
            return -1
        else:
            alturaEsquerda = altura(arbin.esqArbin())
            alturaDireita = altura(arbin.dirArbin())
        if alturaEsquerda > alturaDireita:
            return alturaEsquerda + 1
        else:
            return alturaDireita + 1

    def nivelElemento(arbin:NodeABB, elem):
        if arbin is None:
            return -1
        elif elem == arbin.raizArbin():
            return 0
        elif (elem < arbin.raizArbin() and estaArbin(arbin._esq, elem)):
            return nivelElemento(arbin._esq, elem) + 1

#---------------------------------------------------------------------
# chamada dos metodos implementados
#---------------------------------------------------------------------

nodee = NodeABB()

if(nodee.vaziaArbin):
    print("nodee ta vazio")
#arbin = None
arbin = NodeABB(10) # node que eh a raiz da arvore
preOrdemArbin(arbin)

#inserir 5: criar um no com elem 5
node = NodeABB(5)
#adicionar este node na arbin
arbin.add(node)

# inserir 15
arbin.add(NodeABB(15))

preOrdemArbin(arbin)
print('numero elementos = ', pesoArbin(arbin))

abb = None
abb = insArbinBusca(abb, 100)
abb = insArbinBusca(abb, 45)
abb = insArbinBusca(abb, 200)
abb = insArbinBusca(abb, 300)
abb = insArbinBusca(abb, 250)
preOrdemArbin(abb)

if(estaArbin(abb, 300)):
    print('300 esta na abb')
else:
    print('300 NAO esta na abb')

if(estaArbin(abb, 50)):
    print('50 esta na abb')
else:
    print('50 NAO esta na abb')

print('peso de abb = ', pesoArbin(abb))

a = nivelElemento(abb,300)
print(a)
