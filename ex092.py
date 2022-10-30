from datetime import date
ano = date.today().year
pessoa = {'Nome': input('Nome: ').capitalize(), 
        'Idade': ano - int(input('Ano de nascimento: '))
        }
pessoa['Carteira'] = int(input('Carteira de trabalho[0 se não tiver]: '))
if pessoa['Carteira'] != 0:
    pessoa['Contratado em'] = int(input('Ano de contratação[0 se não tiver]: '))
    pessoa['Salário'] = int(input('Salário: R$'))
    pessoa['Aposentadoria'] = 55 - (ano - pessoa['Contratado em'])
else:
    del pessoa['Carteira']
print('-=' * 30)
for k, v in pessoa.items():
    print(f'{k} = {v}')
