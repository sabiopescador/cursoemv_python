from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Deve se alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para se alistar'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('devera se alistar há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi de {}'.format(ano))