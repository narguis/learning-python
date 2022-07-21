# Says if a given year is a leap year or not

ano = int(input("Digite um ano: "))
unidade = ano // 1 % 10
dezena = ano // 10 % 10
if unidade == 0 and dezena == 0 and ano % 400 == 0:
    print("Esse ano É bissexto!")
elif ano % 4 == 0 and unidade:
    print("Esse ano É bissexto!")
else:
    print("Esse ano NÃO É bissexto!")
