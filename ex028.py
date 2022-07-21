# Gets a random number ranging from 0 to 5 and asks if the reader can find out the chosen
# number, it then congratulates them if they do or wishes them better luck next time
# if they don't

from random import randint
nal = randint(0, 5)
print('\033[33m-=-\033[m'*15)
print('\033[34mVou pensar em um número de 0 a 5\033[m')
print('\033[33m-=-\033[m'*15)
escolha = int(input(f"\033[34mVocê consegue adivinhar qual foi o\033[m \033[1;30;107mnúmero escolhido?\033[m "))
print(f"\033[34mO número escolhido foi \033[m{nal}")
if nal == escolha:
    print("\033[32mParabéns, você acertou o número!\033[m")
else:
    print(f"\033[31mVocê errou o número, eu pensei no {nal}! Mais sorte da próxima vez.\033[m")
