
def fatorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return (n * fatorial(n-1))

def fibonnaci(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fibonnaci(n-2) + fibonnaci(n-1)

def descending(n):
    if n == 1:
        print(f'{n}', end=' ')
    else:
        print(f'{n}', end=' ')
        return descending(n - 1)

def ascending(n):
    if n == 1:
        print(f'{n}', end=' ')
    else:
        ascending(n - 1)
        print(f'{n}', end=' ')

def sumVector(vet, lastPosition):
    if lastPosition == 1:
        return vet[lastPosition - 1]
    else:
        return vet[lastPosition - 1] + sumVector(vet, lastPosition - 1)

if __name__ == "__main__":
    print(f'Função Fatorial: {fatorial(5)}')

    print(f'Função Fibonnaci: {fibonnaci(3)}')

    print(f'Função Descendente:',end=' ')
    descending(5)
    
    print('')
    
    print(f'Função Ascendente:',end=' ')
    ascending(5)

    print('')
    
    print(f'Função Soma Vetor:', end=' ')
    vet = [2,4,6,8,10]
    sumVector(vet, 5)