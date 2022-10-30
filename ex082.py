num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um valor: ')))
    continuar = input('Quer continuar?[S/N] ')
    while continuar.strip()[0] not in 'nNsS':
        continuar = input('Quer continuar?[S/N] ')
    if continuar.strip()[0] in 'nN':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'Lista completa: {num}')
print(f'Lista de pares: {par}')
print(f'Lista de ímpares {impar}')