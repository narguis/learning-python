# Plays a game of rock paper scissors with the reader, with a little bit of roleplay

from random import randint
from time import sleep
# Asks if the reader is ready
print('\033[31mPreparado para uma partida de Pedra, Papel e Tesoura?\033[m')
sleep(2)
pc = randint(1, 3)
# Asks if the reader chooses rock, paper or scissors
ppt = input('\033[31mQual você escolhe, Pedra, Papel ou Tesoura? ')
if ppt.title() == 'Pedra':
    pt = 1
elif ppt.title() == 'Papel':
    pt = 2
elif ppt.title() == 'Tesoura':
    pt = 3
# Calls them a coward if they type anything else
else:
    print('\033[31mDigite Pedra, Papel ou Tesoura, covarde!\033[m')
    pt = 4
sleep(2)
# The computer gets skeptic if it's defeated
if pc == 1 and pt == 2 or pc == 2 and pt == 3 or pc == 3 and pt == 1:
    print('\033[32mNão pode ser... Eu perdi! Você venceu o jogo!\033[m')
# It says it was a good match if it ends in a tie
elif pc == pt:
    print('\033[33mBoa partida, parece que empatamos. Por enquanto...\033[m')
# Wish better luck next time if it's victorious
else:
    print('\033[31mEu venci novamente. Mais sorte na próxima vez\033[m')
# Describes its choice
sleep(1)
# I chose the hard rock
if pc == 1:
    print('Eu escolhi a dura pedra, ', end='')
# I chose the light paper
elif pc == 2:
    print('Eu escolhi o leve papel, ', end='')
# I chose the sharp scissors
else:
    print('Eu escolhi a afiada tesoura, ', end='')
# Says "and so did you", if it ended in a tie
if pt == pc:
    print('assim como você.')
# States the opponent's choice
elif pt == 1:
    print('já você, escolheu a pedra.')
elif pt == 2:
    print('já você, escolheu o papel.')
else:
    print('já você, escolheu a tesoura.')
