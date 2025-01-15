n1 = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento:: '))
n3 = int(input('Terceiro segmento: '))

if n1 >= n2 + n3 or n2 >= n1 + n3 or n3 >= n1 + n2:
    print('NÃO PODE FORMAR UM TRIÂNGULO')

elif n1 != n2 and n1 == n3 or n1 != n3 and n1 == n2:
    print('Triangulo isóceles')

elif n1 == n2 == n3:
    print('TRIANGULO EQUILÁTERO')

else:
    print('TRIANGULO ESCALENO')
