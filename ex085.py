numeros = [[],[]]
for i in range(0, 7):
    n = int(input(f'Digite o {i+1}o valor: '))
    if n % 2 == 0:
        numeros[0].insert(0, n)
    else:
        numeros[1].insert(0, n)
print(f'Números pares: {sorted(numeros[0])}\nNúmeros ímpares: {sorted(numeros[1])}')
