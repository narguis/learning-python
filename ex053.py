# Receives a sentence, print it backwards and check if it's a palindrome

f = str(input("Digite uma frase: "))
s = f.split()
d = f[::-1].split()
j = "".join(s)
g = "".join(d)
print(f"O inverso de '{f}' é '{f[::-1]}'")
if j.lower() == g.lower():
    print(f"'{f}' É um palíndromo!")
else:
    print(f"'{f}' NÃO É um palíndromo!")
