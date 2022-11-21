def leiaDinheiro(msg):
    n = input(msg)
    while n.isnumeric() is False:
        print("\033[31mERRO! Digite um valor monetário válido.\033[m")
        n = input(msg)
    n = float(n)
    return n

def leiaTaxa(msg):
    n = input(msg)
    while n.isnumeric() is False:
        print(f"\033[31mERRO! Digite uma taxa válida.\033[m")
        n = input(msg)
    n = int(n)
    return n