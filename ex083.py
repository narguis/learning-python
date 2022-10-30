expressao = input('Digite sua expressão: ')
if expressao.count('(') == expressao.count(')'):
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')