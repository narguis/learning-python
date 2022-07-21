# Gets a person's name and returns if it contains "Silva" at some point


nome = input("Digite seu nome completo: ")
silva = "silva" in nome.lower()
if silva is True:
    print("Seu nome POSSUI Silva")
else:
    print("Seu nome NÃO POSSUI Silva")
