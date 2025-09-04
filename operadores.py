def adição(n1):
    n2 = int(input('Digite o segundo valor: '))
    risco()
    res= n1 + n2
    return res, n2
   
def subtração(n1):
    n2 = int(input('Digite o segundo valor: '))
    risco()
    res = n1 - n2
    return res, n2

def multiplicação(n1):
    n2 = int(input('Digite o segundo valor: '))
    risco()
    res = n1 * n2
    return res, n2

def divisão(n1):
    n2 = int(input('Digite o segundo valor: '))
    risco()
    res = n1 / n2
    return res, n2
   
def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

def quadrado(n1):
    res = n1 * n1
    return res

def risco():
    print('='*30)