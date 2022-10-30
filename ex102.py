def fatorial(num=1, mostrar=False):
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if mostrar is True:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
    return f


fat = int(input('Você quer calcular o fatorial de qual número? '))
most = (input('Quer ver o cálculo inteiro ou apenas o resultado? [C = Cálculo] e [R = Resultado]: '))
while most.strip()[0] not in 'cCrR':
    print('Resposta inválida!')
    most = (input('Quer ver o cálculo inteiro ou apenas o resultado? [C = Cálculo] e [R = Resultado]: '))
if most.strip()[0] in 'cC':
    most = True
else:
    most = False


print(fatorial(fat, most))
