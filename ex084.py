pessoas = []
individuo = []
peso = []
while True:
    individuo.append(input('Nome: '))
    individuo.append(float(input('Peso: ')))
    pessoas.append(individuo[:])
    peso.append(individuo[1])
    individuo.clear()
    continuar = input('Quer continuar?[S/N] ')

    while continuar.strip()[0] not in 'nNsS':
        continuar = input('Quer continuar?[S/N] ')

    if continuar.strip()[0] in 'nN':
        break

print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {max(peso)}Kg, peso de ', end='')
for p in pessoas:
    if p[1] == max(peso):
        print(f'[{p[0]}]', end=' ')

print(f'\nO menor peso foi {min(peso)}Kg, peso de ', end='')
for p in pessoas:
    if p[1] == min(peso):
        print(f'[{p[0]}]', end=' ')