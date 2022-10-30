def leiaInt(txt):
    num = input(txt)
    while num.strip().isnumeric() is False:
        print('\033[031mErro! Digite um número inteiro válido.\033[m')
        num = input(txt)
    num = int(num)
    return num
    

n = leiaInt("Digite um número: ")
print(f'Você acabou de digitar o número {n}')