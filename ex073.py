times = ('Palmeiras', 'Flamengo', 'Fluminense', 'Corinthians', 'Athletico-PR', 'Internacional', 
'Atlético-MG', 'Santos', 'América-MG', 'Goiás', 'Bragantino', 'Fortaleza', 'São Paulo', 
'Botafogo', 'Ceará SC', 'Coritiba', 'Cuiabá', 'Avaí', 'Atlético-GO', 'Juventude')
print('=-'*20)
print(f'Lista de Times do Brasileirão: {times}')
print('=-'*20)
print(f'Os 5 primeiros são {times[0:5]}')
print('=-'*20)
print(f'Os 4 últimos são {times[-4:]}')
print('=-'*20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-'*20)
print(f'O Fortaleza está na posição {times.index("Fortaleza")+1}')
