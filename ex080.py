num = []
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > num[-1]:
        num.append(n)
    else:
        c = 0
        while c < len(num):
            if n <= num[c]:
                num.insert(c, n)
                break
            c += 1
print(f'Os valores digitados em ordem foram {num}')