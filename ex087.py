matriz = [[0, 0, 0], [0, 0, 0], [0, 0 , 0]]
somapar = somaterc = maiorsegl = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l+1}, {c+1}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    if c == 2:
        somaterc += matriz[l][c]
    if l == 1 and matriz[l][c] > maiorsegl:
        maiorsegl = matriz[l][c]

print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-='*30)

print(f'A soma dos valores pares é {somapar}.')
print(f'A soma dos valores da terceira coluna é {somaterc}.')
print(f'O maior valor da segunda linha é {maiorsegl}.')