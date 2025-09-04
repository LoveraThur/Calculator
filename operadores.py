from math import sqrt
def adição(n1):
    '''-> Função Adição
    -> Calcula a adição de um numero n1 mais um numero n2
    n1: número que veio do programa principal
    n2: número que é pedido para fazer a operação
    res: resultado da operação'''
    n2 = int(input('Digite o segundo valor: '))
    risco()
    res= n1 + n2
    return res, n2
   
def subtração(n1):
    '''-> Função Subtração
    -> Calcula a subtração de um numero n1 menos um numero n2
    n1: número que veio do programa principal
    n2: número que é pedido para fazer a operação
    res: resultado da operação'''
    n2 = int(input('Digite o segundo valor: '))
    risco()
    res = n1 - n2
    return res, n2

def multiplicação(n1):
    '''-> Função Multiplicação
    -> Calcula a multiplicação de um numero n1 por um numero n2
    n1: número que veio do programa principal
    n2: número que é pedido para fazer a operação
    res: resultado da operação'''
    n2 = int(input('Digite o segundo valor: '))
    risco()
    res = n1 * n2
    return res, n2

def divisão(n1):
    '''-> Função Divisão
    -> calcula a divisão de um numero n1 por um numero n2
    n1: número que veio do programa principal
    n2: número que é pedido para fazer a operação
    res: resultado da operação'''
    n2 = int(input('Digite o segundo valor: '))
    risco()
    res = n1 / n2
    return res, n2
   
def fatorial(n):
    '''-> Função Fatorial
    -> calcula o fatorial de um numero n1
    n1: número que veio do programa principal
    f: resultado da operação'''
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

def quadrado(n1):
    '''-> Função Quadrado
    -> Calcula o quadrado de um numero n1
    n1: número que veio do programa principal
    res: resultado da operação'''
    res = n1 * n1
    return res

def raiz(n1):
    '''-> Função Raiz
    ->calcula raiz quadrada de um número n1
    n1: número que veio do programa principal
    res: resultado da operação'''
    res = sqrt(n1)
    return res

def risco():
    '''-> Função Risco
    -> Cria um risco para colocar entre operações ou para quebra de linha no programa principal
    '''
    print('='*30)

