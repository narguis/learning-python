time = []
while True:
    jogador.clear()
    totalgol = 0
    jogador = {'Nome': input('Nome do jogador: ').capitalize(),
            'Gols': [],
    }
    partidas = int(input(f'Quantas partidas o jogador {jogador["Nome"]} jogou? '))
    for i in range(partidas):
        print(' ' * 5, end='')
        gol = int(input(f'Quantos gols na partida {i + 1}? '))
        jogador['Gols'].append(gol)
        totalgol += gol
    jogador['Total'] = totalgol
    time.append(jogador.copy())
    continuar = input('Quer continuar? [S/N] ').strip()[0]
    while continuar not in 'sSnN':
        print('Digite apenas S ou N.')
        continuar = input('Quer continuar? [S/N] ')
    if continuar in 'nN':
        break
print('-=' * 30)
print('Cod.', ' ' * 2, 'Nome', ' ' * 16, 'Gols', ' ' * 10, 'Total')
print('-' * 55)
for i, jog in enumerate(time):
    jog = time[i]['Nome']
    goljog = str(time[i]['Gols'])
    tot = time[i]['Total']
    print(f'{i+1:<8}', end='')
    print(f'{jog:<22}', end='')
    print(f'{goljog:<16}', end='')
    print(f'{tot}')
while True:
    dados = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if dados == 999:
        break
    while dados > len(time) or dados < 0:
        print(f'O jogador {dados} não existe!')
        dados = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if dados == 999:
        break
    lev = time[dados-1]['Nome']
    print(f'Levantamento do jogador {lev}:')
    for i, g in enumerate(time[dados-1]['Gols']):
        print(f'No jogo {i+1} ele fez {g} gols.')
    