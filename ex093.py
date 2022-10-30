jogador = {'nome': input('Nome do jogador: ').capitalize(),
        'gols': list()
}
soma = 0
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(partidas):
    print(' ' * 5, end='')
    gol = int(input(f'Quantos gols na partida {i + 1}? '))
    jogador['gols'].append(gol)
    soma += gol
jogador['total'] = soma
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, g in enumerate(jogador['gols']):
    print(' ' * 5, end='')
    print(f'-> Na partida {i + 1}, ele fez {g} gols.')
print(f'No total, ele fez {jogador["total"]} gols.')
