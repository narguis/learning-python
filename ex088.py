from random import randint
from time import sleep
print('-'*30)
print(' '* 10, 'MEGA-SENA')
print('-'*30)
n = int(input('Quantos jogos você quer sortear? '))
print('-'*30)
print('-=' * 5, f' SORTEANDO {n} JOGOS ', '=-' * 5)
sleep(0.5)
for n in range(0, n):
    megasena = [randint(1, 60), randint(1,60), randint(1, 60), 
    randint(1, 60), randint(1,60), randint(1, 60)]
    print(f'JOGO {n+1}: {megasena}')
    sleep(0.2)
print('-=' * 5, ' BOA SORTE! ', '=-' * 5)
