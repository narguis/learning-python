def contador(inicio, fim, passo):
    for i in range(inicio, fim + 1, passo):
        print(i, end = ' ')
    print()
    print('-=' * 15)

print('Contagem de 1 até 10 de 1 em 1: ')
contador(1, 10, 1)
print('Contagem de 10 até 0 de 2 em 2: ')
contador(10, -2, -2)
print('Personalize a sua contagem: ')
contador(int(input('Ínicio: ')), int(input('Fim: ')), int(input('Passo: ')))
