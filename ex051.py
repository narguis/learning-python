# Arithmetic progression

t = int(input("Primeiro termo: "))
r = int(input("Razão: "))
p = t + (10 - 1) * r
for i in range(t, p, r):
    print(i, end=" -> ")
print("Fim.")
