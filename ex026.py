frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posicação {}'.format(frase.find('A') + 1))
print('A ultima letra A apreceu na posição {}'.format(frase.rfind('A') + 1))
