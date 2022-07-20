# How much will one pay for a rented car, based on the amount of time he spent with it
# and how many kilometers he drove.

dias = int(input("\033[33mPor quantos dias o carro foi alugado?\033[m "))
km = int(input("\033[34mQuantos quilômetros foram percorridos?\033[m "))
print(f"O total a pagar é \033[32mR${(dias*60)+km*0.15}\033[m")
