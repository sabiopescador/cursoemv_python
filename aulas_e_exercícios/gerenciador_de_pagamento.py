'''
    elabore um pprograma que calcule o valor a ser pago por um produto,
    considerendo o seu preço normal e condição de pagamento:

    à vista, dinheiro/cheque:
    10% de desconto

    à vista no cartão: 5% de desconto

    em até 2x no catão: preço normal

    3x ou mais no cartão: 20% de juros

'''

valor = float(input('Valor a ser pago R$: '))

print('OPÇÕES: \n')

print('[1] à vista, dinheiro/cheque')
print('[2] à vista no cartão')
print('[3] em até 2x no catão')
print('[4] 3x ou mais no cartão\n')

opção = int(input(': '))
compra = 0

if opção == 1:
    compra = valor - (valor*10/100)
    print('sua compra de {:.2f} vai custar {:.2f}'.format(valor, compra))
    
elif opção == 2:
    compra = valor - (valor*5/100)
    print('sua compra de {:.2f} vai custar {:.2f}'.format(valor, compra))

elif opção == 3:
    compra = valor/2
    print('Compra parcelada em 2x no cartão.')
    print('sua compra de {:.2f} vai custar {:.2f}'.format(valor, compra))

elif opção == 4:
    parcelas = int(input('Quantas parcelas vão ser ? '))
    
    compra = valor + ((valor*20)/100)
    divisão = (valor + ((valor*20)/100))/parcelas

    print(f'Sua compra parcelada em {parcelas}x de {divisão:.2f} COM JUROS')
    print('sua compra de {} vai custar {:.2f}'.format(valor, compra))
else:
    compra = 0
    print('\033[31mOPÇÃO INVÁLIDA !\033[m')
    print(F'TOTAL = {compra:.2f}')