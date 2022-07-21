# New salary of an employee with a 10% raise if they already make more than 1250
# and a 15% raise if they don't

salario = float(input("Qual é o seu salário? "))
dez = salario*(10/100)
quinze = salario*(15/100)
if salario > 1250:
    print(f"Após o reajuste, seu novo salário será de R${salario+dez}!")
else:
    print(f"Após o reajuste, seu novo salário será de R${salario+quinze}!")
