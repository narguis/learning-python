def lerInt():
    while True:
        try:
            n = int(input("Digite um valor inteiro: "))
        except (ValueError, TypeError):
            print("\033[31mDigite um número inteiro válido!\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[34mEntrada de dados interrompida pelo usuário.\033[m")
            return 0
        else:
            return n

def lerFloat():
    while True:
        try:
            n = float(input("Digite um valor real: "))
        except (ValueError, TypeError):
            print("\033[31mDigite um número real válido!\033[m")
        except (KeyboardInterrupt):
            print("\n\033[34mEntrada de dados interrompida pelo usuário.\033[m")
            return 0
        else:
            return n
