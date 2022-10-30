pessoa = {'Nome': input('Nome: ').capitalize() , 'Média': float(input('Média: '))}
if pessoa['Média'] > 7:
    pessoa['Situação'] = 'Aprovado'
elif pessoa['Média'] > 5:
    pessoa['Situação'] = 'Recuperação'
else:
    pessoa['Situação'] = 'Reprovado'
print('-=' * 30)
for k, v in pessoa.items():
    print(' ' * 5 + '-> ', end='')
    print(f'{k} = {v}')