n1 = n2 = n3 = n4 = -1
while n1 < 0 or n1 > 10:
    n1 = int(input("Digite um valor entre 0 e 10: "))
while n2 < 0 or n2 > 10:
    n2 = int(input("Digite outro valor entre 0 e 10: "))
while n3 < 0 or n3 > 10:
    n3 = int(input("Digite mais um valor entre 0 e 10: "))
while n4 < 0 or n4 > 10:
    n4 = int(input("Digite o último valor entre 0 e 10: "))
tupla = (n1, n2, n3, n4)
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if n1 == 3 or n2 == 3 or n3 == 3 or n4 == 3:
    print(f'O número 3 apareceu na posição {tupla.index(3)+1}.')
else:
    print(f'O número 3 não foi digitado em nenhuma posição.')
if n1 % 2 == 0 or n2 % 2 == 0 or n3 % 2 == 0 or n4 % 2 == 0:
    print('Os números pares digitados foram: ', end='')
    if n1 % 2 == 0:
        print(n1, end=' ')
    if n2 % 2 == 0:
        print(n2, end=' ')
    if n3 % 2 == 0:
        print(n3, end=' ')
    if n4 % 2 == 0:
        print(n4, end=' ')
else:
    print('Nenhum número par foi digitado!')