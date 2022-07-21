# Calculates if three lines can form a triangle and if they do, says if it's an
# equilateral, isosceles or scalene triangle

a = float(input('Tamanho da primeita reta: '))
b = float(input('Tamanho da segunda reta: '))
c = float(input('Tamanho da terceira reta: '))
ab = a - b
bc = b - c
ac = a - c
condab = a - b < c < a + b
condac = a - c < b < a + c
condbc = b - c < a < b + c
condmodab = ab * -1 < c < a + b
condmodac = ac * -1 < b < a + c
condmodbc = bc * -1 < a < b + c
if condab or condmodab and condac or condmodac and condbc or condmodbc is True:
    print('\033[32mEssas retas PODEM formar um triângulo', end=" ")
    if a == b and a == c:
        print('equilátero.')
    elif a == b or a == c or b == c:
        print('isósceles.')
    else:
        print('escaleno.')
else:
    print('\033[31mEssas retas NÃO PODEM formar um triângulo.\033[m')
