print('=' * 10,'LOJA NASCIMENTO','=' * 10)
print('FORMAS DE PAGAMENTO')
preco = int(input('Qual o valor da compra: '))
print('''
[ 1 ] á vista  dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
opcao = int(input('Qual é a opção? '))
if opcao == 1 :
    descontoavista = preco - (preco * 10 / 100)
    print('Sua compra de {} vai custar {}'.format(preco, descontoavista))
elif opcao == 2 :
    descontocartao = (preco * 5 / 100)
    print('Sua compra de {} vai custar {}'.format(preco, descontocartao))
elif opcao == 3 :
    semdesconto = preco / 2
    print('Sua compra de {} vai custar {}'.format(preco,semdesconto))
elif opcao == 4 :
    comjuros = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = comjuros / totalparc
    print('Sua compra sera parcelada em {}X de {:.2f} R$'.format(totalparc, parcela))
    print('Sua compra de {} vai custar {} no final'.format(preco, comjuros))
