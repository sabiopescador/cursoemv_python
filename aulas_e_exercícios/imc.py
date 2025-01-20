peso = (float(input('Digite o seu peso: ')))
altura = (float(input('Digite a altura: ')))

imc = peso / (altura ** 2)

print('O SEU IMC É DE {:.2f}'.format(imc))

if imc < 18.5:
    print('ABAIXO DO PESO')

elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL')

elif imc >= 25 and imc < 30:
    print('SOBREPESO')

elif imc >= 30 and imc <= 40:
    print('Obesidade')

else:
    print('OBESIDADE MÓRBIDA')
