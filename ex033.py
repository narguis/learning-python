# Gets the biggest and smallest numbers out of 3 given values

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))
if n1 > n2 and n1 > n3:
    print(f"{n1} é o maior valor e ", end="")
elif n2 > n1 and n2 > n3:
    print(f"{n2} é o maior valor e ", end="")
else:
    print(f"{n3} é o maior valor e ", end="")
if n1 < n2 and n1 < n3:
    print(f"{n1} é o menor valor!")
elif n2 < n1 and n2 < n3:
    print(f"{n2} é o menor valor!")
else:
    print(f"{n3} é o menor valor!")
