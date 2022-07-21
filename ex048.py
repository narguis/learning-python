# How many multiples of 3 are between 1 and 500 and what's the value of their sum

s = 0
v = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i
        v += 1
print(f"A soma dos {v} valores é {s}.")
