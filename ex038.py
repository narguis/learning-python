# Receives two values and checks if they're equal. If they're not, it'll print
# the greater value

v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
if v1 > v2:
    print(f'\033[32m{v1} é maior que {v2}!\033[m')
elif v2 > v1:
    print(f'\033[31m{v2} é maior que {v1}!\033[m')
else:
    print(f'\033[34mAmbos os valores são iguais!\033[m')
