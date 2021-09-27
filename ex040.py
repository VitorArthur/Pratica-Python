n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, media))
if media < 5:
    print('\033[31mREPROVADO\033[m')
elif media >= 5 and media <= 7:
    print('\033[32mRECUPERAÇÃO\033[m')
else:
    print('\033[34mAPROVADO\033[m')