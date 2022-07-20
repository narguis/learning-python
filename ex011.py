# Find out how many cans of paint will you need to paint a wall using it's height and width

lar = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
print(f"A área da sua parede é de \033[35m{alt*lar:.2f}\033[m metros quadrados\n"
      f"Você precisará de \033[33m{(alt*lar)/2:.2f}\033[m litros de tinta para pintá-la")
