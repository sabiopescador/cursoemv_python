# crie um programa que leia uma cidade e diga se ela começa ou não com o nome "SANTO"

cid = str(input('Em que cidde você nasceu? ')).strip() # método para separas espaços
print(cid[:5].upper() == 'SANTO')
