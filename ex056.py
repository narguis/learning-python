homemmaisvelho = ''
mulheresvinte = 0
idadetotal = 0
maioridade = 0
for i in range(1, 5):
    print('-'*10+f'{i} PESSOA'+'-'*10)
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    idadetotal += idade
    sexo = input('Sexo [M/F]: ').strip()
    if sexo not in 'Ff' and sexo not in 'Mm':
        print('Digite um sexo válido!')
        break
    if sexo in 'Ff' and idade < 20:
        mulheresvinte += 1
    if idade > maioridade and sexo in 'Mm':
        maioridade = idade
        homemmaisvelho = nome
media = (idadetotal/4)
print(f'A média de idade do grupo é de {media} anos.\n'
      f'O homem mais velho tem {maioridade} anos e se chama {homemmaisvelho}.\n'
      f'Ao todo são {mulheresvinte} mulheres com menos de 20 anos.')