pessoas = []
mulheres = []
cadastro ={}
continuar = '0'
idgeral = 0
while continuar not in 'nN':
    cadastro['nome'] = input('Nome: ').capitalize()
    cadastro['sexo'] = input('Sexo: [M/F] ').upper()
    while cadastro['sexo'] not in 'mMfF':
        print('Por favor, digite apenas M ou F.')
        cadastro['sexo'] = input('Sexo: [M/F] ').upper()
    if cadastro['sexo'] in 'fF':
        mulheres.append(cadastro['nome'])
    cadastro['idade'] = int(input('Idade: '))
    idgeral += cadastro['idade']
    pessoas.append(cadastro)
    continuar = input('Quer continuar? [S/N] ')
    while continuar not in 'sSnN':
        print('Por favor, digite apenas S ou N.')
        continuar = input('Quer continuar? [S/N] ')
media = idgeral / len(pessoas)
print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media} anos.')
print(f'C) As mulheres cadastradas foram {mulheres}.')
print(f'D) Lista de pessoas que estão acima da média de idade: ')
for i, p in enumerate(pessoas):
    if pessoas[i]['idade'] > media:
        print(p)
