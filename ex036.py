# Calculates if you're allowed to get a bank loan based on a few factors

print("\033[34mBem-vindo ao simulador de empréstimo bancário!\033[m")
# The value of the loan, or the price of the house you're going to use it to buy
valor = int(input("\033[33mQual o valor da casa que você deseja comprar?\033[m "))
# Your monthly salary
salario = int(input('\033[32mQual é o seu salário mensal?\033[m '))
# In how many years do you plan to pay back the loan
tempo = int(input("\033[36mEm quantos anos você planeja pagar?\033[m "))
# Checks if you'd have to pay more than 30% of your monthly salary
maximo = (30/100) * salario
prestacao = valor/(tempo*12)
# Denies or accepts the loan request based on the percentage
if prestacao > maximo:
    print('\033[31mO empréstimo será NEGADO!\033[m')
else:
    print('\033[32mO empréstimo será APROVADO!\033[m')
