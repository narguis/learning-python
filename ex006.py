# Get the double, triple and square root of a given number

from math import sqrt
numero = int(input("Digite um número: "))
cores = {"vermelho": "\033[31m",
         "limpa": "\033[m",
         "roxo": "\033[35m"}
print(f"O dobro de {cores['vermelho']}{numero}{cores['limpa']} é {cores['roxo']}{numero*2}{cores['limpa']}\n"
      f"O triplo de {cores['vermelho']}{numero}{cores['limpa']} é {cores['roxo']}{numero*3}{cores['limpa']}\n"
      f"A raiz quadrada de {cores['vermelho']}{numero}{cores['limpa']} é {cores['roxo']}{sqrt(numero):.2f}{cores['limpa']}")
