# Checks if a given number is a prime number, and if it's not, shows how many
# dividers it has

n = int(input("Digite um número: "))
j = 0
for i in range(1, n+1):
    if n % i == 0:
        j += 1
if j > 2:
    print(f"O número {n} não é primo, pois possui {j} divisores.")
else:
    print(f"O número {n} é primo, pois só é divisível por 1 e por {n}.")
