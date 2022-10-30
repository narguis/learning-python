from datetime import date
def voto(ano):
    idade = date.today().year - ano
    print(f'Com {idade} anos: ', end='')
    if (idade < 18 and idade > 16) or idade > 65:
        return 'VOTO OPCIONAL'
    elif idade < 16:
        return 'NÃO VOTA'
    else:
        return 'VOTO OBRIGATÓRIO'

nasc = int(input('Em que ano você nasceu? '))
while date.today().year - nasc < 0:
    print('Data inválida!')
    nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))