n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))

media = (n1 + n2) / 2

print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, media))

if media >= 6.0:
    print('APROVADO')
elif media < 6.0 and media > 5.5:
    print('ALUNO EM RECUPERAÇÃO')
else:
    print('REPROVADO')
