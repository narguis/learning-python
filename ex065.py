n = soma = maior = menor = conta = 0
continuar = ""
while continuar.upper() != 'N':
    n = int(input("Digite um número: "))
    continuar = input("Quer continuar?[S/N] ").strip()[0]
    soma += n
    conta += 1
    if n > maior:
        maior = n
    if menor == 0:
        menor = n
    elif menor > n:
        menor = n
print(f"Você digitou {conta} valores e a média entre eles foi de {soma/conta}.")
print(f"O maior valor foi {maior} e o menor valor foi {menor}.")
