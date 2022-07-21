# Asks for the body weight of 5 people and prints the greater and smaller values

maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i} pessoa: "))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso foi de {maior}kg.\nO menor peso foi de {menor}kg.")
