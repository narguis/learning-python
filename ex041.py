# Category a swimmer will compete in depending on its year of birth

ano = int(input('Digite o ano de nascimento do nadador: '))
idade = 2022 - ano
mensagem = 'Você irá competir na categoria '
if idade <= 9:
    print(f'{mensagem}MIRIM!')
elif idade <= 14:
    print(f'{mensagem}INFANTIL!')
elif idade <= 18:
    print(f'{mensagem}JUNIOR!')
elif idade <= 20:
    print(f'{mensagem}SÊNIOR!')
else:
    print(f'{mensagem}MASTER!')
