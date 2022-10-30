pessoas = list()
p = ['', 0, 0]
while True:
    p[0] = input('Nome: ').strip().capitalize()
    p[1] = float(input('Nota 1: '))
    while p[1] > 10 or p[1] < 0:
        print('Nota inválida!')
        p[1] = float(input('Nota 1: '))
    p[2] = float(input('Nota 2: '))
    while p[2] > 10 or p[2] < 0:
        print('Nota inválida!')
        p[2] = float(input('Nota 2: '))
    pessoas.append(p[:])

    cont = input('Quer continuar?[S/N] ')
    while cont.strip()[0] not in 'sSnN':
        cont = input('Quer continuar?[S/N] ')
    if cont.strip()[0] in 'nN':
        break

print('-=' * 15)
print('No. NOME', ' ' * 10, 'MÉDIA')
print('-' * 30)

# Outro jeito de fazer
'''for i in range(0, len(pessoas)):
    media = (pessoas[i][1] + pessoas[i][2])/2
    print(f'{i+1}  ', f'{pessoas[i][0]:<15}', f'{media:<5.1f}')'''

for c, i in enumerate(pessoas):
    media = (i[1] + i[2])/2
    print(f'{c+1}  ', f'{i[0]:<15}', f'{media:<5.1f}')
print('-' * 50)

while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    print('-' * 50)
    if aluno == 999:
        break
    elif aluno - 1 > len(pessoas):
        print('Aluno inexistente!')
        print('-' * 50)
    else:
        print(f'As notas de {pessoas[aluno - 1][0]} são {pessoas[aluno - 1][1:]}.')