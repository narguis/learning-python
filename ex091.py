from random import randint
from time import sleep
from operator import itemgetter
dados = {'jogador1': 0, 'jogador2': 0, 'jogador3': 0, 'jogador4': 0}
print('Valores sorteados:')
sleep(1)
for jogador, dado in dados.items():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    dados[jogador] = dado1 + dado2
    print(f'O {jogador} tirou {dado1} e {dado2} nos dados.')
    sleep(1)
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
ranking = sorted(dados.items(), key = itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar = {v[0]} com {v[1]} pontos.')
    sleep(1)
