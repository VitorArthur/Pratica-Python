casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Quantos anos de financiameto? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end= '0')
print('A prestação será de R${}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')