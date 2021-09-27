print('\033[34m-=-\033[m' * 20)
print('\033[30;41mAnalizador de Triângulos\033[m')
print('\033[34m-=-\033[m' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r2 + r1:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulos!')
