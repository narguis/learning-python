produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 
'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 22.3, 'Livro', 34.9)
print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*50)
for n in range(0, len(produtos)):
    if n % 2 == 0:
        print(f'{produtos[n]:-<42}', end='')
    else:
        print(f'R${produtos[n]:>6.2f}')
print('-'*50)