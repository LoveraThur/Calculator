import operadores   
ops = ('+','-','x','/','!','q')

def calculadora():
    operadores.risco()
    print('CALCULADORA'.center(30))
    operadores.risco()
    n = int(input('Digite o primeiro número: '))
    operadores.risco()
    print(' [+] [-] [x] \n [/] [!] [Q]\n')
    op = ' '
    while op not in ops:
        op = str(input('Operação desejada: ')).lower()
    operadores.risco()
    if op == '+':
        a = operadores.adição(n)
        print(f'{n} + {a[1]} = {a[0]}')
    elif op == '-':
        s = operadores.subtração(n)
        print(f'{n} - {s[1]} = {s[0]}')
    elif op == 'x':
        m= operadores.multiplicação(n)
        print(f'{n} x {m[1]} = {int(m[0])}')
    elif op == '/':
        div = operadores.divisão(n)
        print(f'{n} / {div[1]} = {div[0]}')
    elif op == 'q':
        print(f'{n} x {n} = {operadores.quadrado(n)}')
    else:
        print(f'{n}! = {operadores.fatorial(n)}')
calculadora()