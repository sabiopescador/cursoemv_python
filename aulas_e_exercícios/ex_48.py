# Soma ímpares múltiplos de três no intervalo de 1 a 500

n = 0
cont = 0
inicio = 10
fim = 1000

for i in range (inicio,fim):
    if i%2 !=0 and i%3 == 0:
        n+=i
        cont +=1

print('A soma dos {} multiplos de 3 no intervalo de {} a {} é igual a: {}'.format(cont,inicio,fim, n))