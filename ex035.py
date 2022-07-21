# Receives three lines respective lengths and calculates if they can form a triangle

r1 = float(input("Tamanho da primeira reta: "))
r2 = float(input("Tamanho da segunda reta: "))
r3 = float(input("Tamanho da terceira reta: "))
ab = r1 - r2
ac = r1 - r3
bc = r2 - r3
abm = ab < r3 < r1 + r2
acm = ac < r2 < r1 + r3
bcm = bc < r1 < r2 + r3
modab = ab * -1 < r3 < r1 + r2
modac = ac * -1 < r2 < r1 + r3
modbc = bc * -1 < r1 < r2 + r3
if abm or modab and acm or modac and bcm or modbc == True:
    print("Essas conjunto de retas PODE formar um triângulo.")
else:
    print("Esse conjunto de retas NÃO PODE formar um triângulo")
print(abm, modab)
print(acm, modac)
print(bcm, modbc)
