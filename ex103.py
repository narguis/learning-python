def ficha(jog = '<desconhecido>', gols = 0):
    print(f"O jogador {jog} fez {gols} gols.")

j = input('Nome do jogador: ')
n = (input('Número de gols: '))
if n.isnumeric():
    n = int(n)
else:
    n = 0
if j.strip() == '':
    ficha(gols = n)
else:
    ficha(j, n)