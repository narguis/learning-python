num = []
for i in range(0, 5):
    print(f'Digite um valor para a posição {i}: ', end='')
    num.append(int(input()))
print('=-'*30)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {max(num)} nas posições ', end='')
for c, n in enumerate(num):
    if n == max(num):
        print(c, end=' ')
print(f'\nO menor valor digitado foi {min(num)} nas posições ', end='')
for c, n in enumerate(num):
    if n == min(num):
        print(c, end=' ')