from time import sleep

while True:
    print('-' * 30)
    print('Sistema de ajuda PyHelp')
    print('-' * 30)
    sleep(0.5)
    func = input('Função ou Biblioteca > ')
    if func == 'fim':
        print('Sistema finalizado!')
        break
    else:
        print(help(func))