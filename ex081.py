num = []
while True:
    num.append(int(input('Digite um valor: ')))
    cont = input('Quer continuar?[S/N] ')
    while cont.strip()[0] not in 'sSnN':
        cont = input('Quer continuar?[S/N] ')
    if cont.strip()[0] in 'nN':
        break
print('-='*30)
print(f'Você digitou {len(num)} elementos.')
print(f'Os valores em ordem decrescent são {sorted(num, reverse=True)}')
if 5 in num:
    print(f'O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte dessa lista.')
