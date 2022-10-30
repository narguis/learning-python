from random import randint
números = []
def sorteia():
    números.clear()
    for i in range(5):
        números.append(randint(1, 10))
    print(f'Os 5 valores sorteados foram {números}.')

def somapar():
    soma = 0
    for n in números:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares, temos {soma}.')

sorteia()
somapar()