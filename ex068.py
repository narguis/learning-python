from random import randint
print("PAR OU ÍMPAR")
print("-"*20)
parimpar = ''
resultado = ''
vitoria = 0
while parimpar.upper() == resultado:
    pc = randint(0, 10)
    n = int(input("Digite um número de 0 a 10: "))
    while n > 10 or n < 0:
        n = int(input("Digite um número de 0 a 10: "))
    soma = pc+n
    parimpar = input("Par ou Ímpar?[P/I] ").strip()[0]
    while parimpar not in 'pPiI':
        parimpar = input("Par ou Ímpar?[P/I] ").strip()[0]
    if soma % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    if parimpar.upper() == resultado:
        print("Parabéns, você venceu! ", end='')
        vitoria += 1
    else:
        print("Que pena, você perdeu! ", end='')
    print(f"Você escolheu {n} e o computador {pc}. O total é {soma}, um número ",end='')
    if resultado == 'P':
        print("PAR.")
    elif resultado == 'I':
        print("ÍMPAR.")
    if parimpar.upper() == resultado:
        print("Vamos jogar novamente!")
print(f"Acabou! Você venceu {vitoria} vezes.")
