# Receives a natural number up to 4 digits long
# Returns its units, dozens, hundreds and thousands places, separately.

num = int(input("Digite um número de 0 a 9999: "))
print(f"Unidade: {num // 1 % 10}")
print(f"Dezena: {num // 10 % 10}")
print(f"Centena: {num // 100 % 10}")
print(f"Milhar: {num // 1000 % 10 }")
