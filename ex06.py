frase = str(input('Digite uma frase: ')).upper()
a = frase.count('A')
p = frase.find('A')+1
u = frase.rfind('A')+1
print(f'A letra A aparece {a} vezes na frase')
print(f'A primeira letra A apareceu na posição {p}')
print(f'A última letra A apareceu na posição {u}')