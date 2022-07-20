# Truncating a float input to get the whole part

from math import trunc
valor = float(input("\033[36mDigite um valor:\033[m "))
print(f"A parte inteira do número \033[36m{valor}\033[m é \033[35m{trunc(valor)}\033[m")
