n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    maior = n1
    print('O\033[34m MAIOR\033[m número é {}'.format(maior))
elif n2 > n1:
    maior = n2
    print('O \033[34mMAIOR\033[m número é {}'.format(maior))
elif n1 == n2:
    print('\033[34mNÃO\033[m exite numero maior, os dois são iguais!')
