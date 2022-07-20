# How much will an employee be paid if they get a 15% raise

salario = float(input("\033[34mQual é o salário do funcionário?\033[m "))
aumento = salario+(salario*(15/100))
print(f"O funcionário que ganhava \033[31mR${salario}\033[m, com um aumento de \033[32m15%\033[m "
      f"passa a ganhar \033[32m{aumento}\033[m")
