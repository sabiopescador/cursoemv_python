# classificando atletas

ano_nasc = int(input('Ano de Nascimento: '))
ano_atual = 2025
idade = ano_atual - ano_nasc
print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação: Junior')
elif idade > 19 and idade <= 25:
    print('Classificação: Sênior')
else:
    print('Classificação: MASTER')
