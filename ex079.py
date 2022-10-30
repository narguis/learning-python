num = []
continuar = 't'
while True:
    n = int(input('Digite um valor: '))
    if n in num:
        print('Não posso adicionar valores duplicados!')
    else:
        num.append(n)
        print('Valor adicionado com sucesso!')
    continuar = input('Quer continuar?[S/N] ')
    while continuar.strip()[0] not in 'nNsS':
        continuar = input('Quer continuar?[S/N] ')
    if continuar.strip()[0] in 'nN':
        break
print('-='*30)
num.sort(reverse=False)
print(f'Você digitou os valores {num}')