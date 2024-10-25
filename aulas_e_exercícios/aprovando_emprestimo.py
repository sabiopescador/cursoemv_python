
print('APROVANDO EMPRESTIMO!')


print("Vamos começar o cálculo de prestações da casa, ensira alguns dados..")


valor_casa = float(input('INFORME O VALOR TOTAL DA CASA: \n'))

salario_comprador = float(input('AGORA INFORME O SEU SALÁRIO: \n'))

anos = int(input('EM QUANTOS ANOS VOCÊ PRETENDE PAGAR A SUA CASA ? \n'))

parcela_anual = valor_casa / anos 
parcela_mensal = parcela_anual / 12
porcentagem = salario_comprador * 30/100

print('Valor Mínimo da parcela do imóvel = [{:.2f}]\n'.format(parcela_mensal))
print(f'Com 30% de R$:{salario_comprador} você poderá pagar R$:{porcentagem}\n')


if parcela_mensal <= porcentagem:
    print('PARABÉNS, SEU EMPRÉSTIMO FOI APROVADO!')
else:
    print(f'DESCULPE MAS O VALOR DE{porcentagem}NÃO É O SUFICIENTE PARA PAGAR UMA PARCELA DO FINANCIAMENTO..')
