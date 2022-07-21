# Calculates if a given person will receive a traffic ticket and if they do, how much
# will they have to pay.

print("O limite de velocidade é de 80km/h!")
km = int(input("A quantos km/h estava o último carro? "))
multa = (km-80)*7
if km <= 80:
    print("Sem problemas!")
else:
    print(f"O carro foi multado em R${multa}! Mais atenção na próxima.")
