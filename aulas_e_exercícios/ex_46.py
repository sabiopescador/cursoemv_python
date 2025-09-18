from time import sleep
# fazer uma contagem regrassiva
n = int(input('digite um númreo: '))

for i in range(n, -1, -1):
    print(n)
    sleep(0.5)
    n -= 1

print('KABUM!!')