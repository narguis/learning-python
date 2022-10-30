print("TABUADA (Digite um número negativo para parar)")
print("-"*50)
while True:
    tabuada = int(input("Quer ver a tabuada de qual valor? "))
    if tabuada < 0:
        break
    for i in range(1, 11):
        print(f"{tabuada} X {i} = {tabuada*i}")
    print("-"*50)
print("Programa encerrado.")
