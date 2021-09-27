r1 = float(input('PRIMEIRO SEGMENTO: '))
r2 = float(input('SEGUNDO SEGMENTO: '))
r3 = float(input('TERCEIRO SEGMENTO: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUÍLATERO')
    elif r1 == r2 != r3 or r1 == r3 != r2:
        print('Os segmentos acima NÃO PODEM formar um triângulo')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')