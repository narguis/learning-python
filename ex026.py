# Gets how many times the letter "a" shows up in a sentence and when did it first
# and last appear

frase = input("Digite uma frase: ").lower()
letra = frase.count("a")
posicao = frase.find("a")+1
contrario = frase.rfind("a")+1
print(f"A letra >A< aparece {letra} vezes na sua frase\n"
      f"Ela aparece pela primeira vez na posição {posicao}\n"
      f"Ela aparece pela última vez na posição {contrario}")
