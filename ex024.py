# Gets a city name and returns if it starts with "Santo" or not

cid = input("Digite o nome da sua cidade: ")
santo = "santo" in cid.lower().split()[0]
if santo is True:
    print("Sua cidade COMEÇA com Santo.")
else:
    print("Sua cidade NÃO COMEÇA com Santo.")
