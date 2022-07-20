# Calculate the mean between two grades an show if the student will pass or fail

n1 = float(input("Primeira nota do aluno: "))
n2 = float(input("Segunda nota do aluno: "))
md = (n1+n2)/2
if n1 < 6 and n2 < 6:
    print(f"A média entre \033[31m{n1}\033[m e \033[31m{n2}\033[m é \033[31m{md}\033[m.")
elif n1 < 6 and md < 6:
    print(f"A média entre \033[31m{n1}\033[m e \033[32m{n2}\033[m é \033[31m{md}\033[m.")
elif n2 < 6 and md < 6:
    print(f"A média entre \033[32m{n1}\033[m e \033[31m{n2}\033[m é \033[31m{md}\033[m.")
elif n1 < 6:
    print(f"A média entre \033[31m{n1}\033[m e \033[32m{n2}\033[m é \033[32m{md}\033[m.")
elif n2 < 6:
    print(f"A média entre \033[32m{n1}\033[m e \033[31m{n2}\033[m é \033[32m{md}\033[m.")
else:
    print(f"A média entre \033[32m{n1}\033[m e \033[32m{n2}\033[m é \033[32m{md}\033[m.")
if md >= 6:
    print("Você foi \033[32mAPROVADO\033[m!")
else:
    print("Você foi \033[31mREPROVADO\033[m!")
