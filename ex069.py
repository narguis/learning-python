dezoito = homens = mulhervinte = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        dezoito += 1
    sexo = input('Sexo[M/F]: ').strip()[0]
    while sexo not in 'mMfF':
        print('SEXO INVÁLIDO!')
        sexo = input('Sexo[M/F]: ').strip()[0]
    if sexo.upper() == 'M':
        homens += 1
    elif sexo.upper() == 'F' and idade < 20:
        mulhervinte += 1 
    continuar = input("Quer continuar?[S/N]: ").strip()[0]
    while continuar not in 'sSnN':
        print('OPÇÃO INVÁLIDA!')
        continuar = input("Quer continuar?[S/N]: ").strip()[0]
    if continuar in 'nN':
        break
print(f'{dezoito} pessoas com mais de 18 anos foram registradas.')
print(f'{homens} homens foram registrados.')
print(f'{mulhervinte} mulheres com mennos de 20 anos foram registradas.')
