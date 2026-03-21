from operadores import *  
ops = ('+','-','x','/','!','q','r')

def calculadora():
    risco()
    print('CALCULADORA'.center(30))
    risco()
    while True:
        try:
            n = float(input('Digite o primeiro número: '))
        except:
            print('\033[31mNúmero Inválido. Tente novamente\033[m')
            risco()
        else:
            break
    risco()
    print(' [+] [-] [x] \n [/] [!] [Q]\n [R]')
    op = ' '
    while op not in ops:
        try:
            op = str(input('Operação desejada: ')).lower()
        except:
            print('\033[31m\nDigite uma Opção válida\033[m')
    risco()
    if op == '+':
        a = adicao(n)
        print(f'{n} + {a[1]} = {a[0]}')
    elif op == '-':
        s = subtracao(n)
        print(f'{n} - {s[1]} = {s[0]}')
    elif op == 'x':
        m= multiplicacao(n)
        print(f'{n} x {m[1]} = {float(m[0]):.1f}')
    elif op == '/':
        div = divisao(n)
        print(f'{n} / {div[1]} = {div[0]}')
    elif op == 'q':
        print(f'{n} x {n} = {quadrado(n)}')
    elif op == 'r':
        print(f'√{n} = {raiz(n)}')
    else:
        print(f'{n}! = {fatorial(n)}')
calculadora()