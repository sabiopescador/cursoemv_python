# procurando uma string dentro de outra

'''
    print('Seu nome tem silva? {}'.format('silva' in nome.lower()))
'''
nome = str(input('Qual o seu nome completo? ')).strip().upper()

if nome.find('SILVA') != -1:
    condição = '*SIM*'
else:
    condição = '*NÃO*'

print('Seu nome tem silva? {}'.format(condição))