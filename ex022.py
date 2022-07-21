# Count the letters in a string without the spaces

nome = str(input("Digite seu nome completo: ")).strip()
div = "".join(nome.split())
posicao = nome.split()
print(f"Seu nome maiúsculo é: {nome.upper()}")
print(f"Seu nome minúsculo é: {nome.lower()}")
print(f"Seu nome possui {len(div)} letras")
print(f"Seu primeiro nome é {posicao[0]} e possui {len(posicao[0])} letras")
