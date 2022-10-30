from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram ', end='')
for n in tupla:
    print(f'{n} ', end='')
print(f'\nO maior foi {max(tupla)}.\nO menor foi {min(tupla)}.')
