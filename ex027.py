# Receives a full name and returns first and last name

nome = input("Digite seu nome completo: ")
divisao = nome.split()
print(f"Seu primeiro nome é {divisao[0]} e seu último nome é {divisao[1]}")
