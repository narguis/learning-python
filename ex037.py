# Converts a number to binary, octal and hexadecimal system

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} em BINÁRIO é {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} em OCTAL é {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} em HEXADECIMAL é {hex(num)[2:]}')
else:
    print('Digite 1, 2 ou 3!')
