# Receives the year of birth of 7 different people and prints
# how many of them are over and under 18

from datetime import date
ano = date.today().year
mn = 0
ma = 0
for i in range(1, 8):
    z = int(input(f"Ano em que a {i} pessoa nasceu: "))
    if ano-z < 18:
        mn += 1
    else:
        ma += 1
print(f"Neste grupo há {ma} pessoas maiores de idade e {mn} pessoas menores de idade.")

