peso = float(input('Qual seu peso (kg)'))
altura = float(input('Qual a sua altura? (m)'))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f}, e seu status é '.format(imc),end='')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
elif imc > 40:
    print('OBSIDADE MÓRBIDA')
