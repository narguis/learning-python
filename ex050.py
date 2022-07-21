# Receives six integers, discard the odd ones
# Shows how many even number there are and their sum

s = 0
v = 0
for i in range(1, 7):
    n = int(input("Digite um valor: "))
    if n % 2 == 0:
        s += n
        v += 1
print(f"A soma dos {v} valores é {s}.")
