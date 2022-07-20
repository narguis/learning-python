# Showcase the sum between two numbers

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
limpa = "\033[m"
print(f"A soma entre \033[31m{n1}{limpa} e \033[36m{n2}{limpa} é \033[35m{n1+n2}{limpa}")
