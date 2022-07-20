# Convert distances from meters to kilometers and other units

distancia = float(input("Digite uma distância em metros: "))
azl = "\033[34m"
fim = "\033[m"
print(f"A distância de {azl}{distancia}{fim} metros corresponde a:\n"
      f"{azl}{distancia/1000}{fim}km\n"
      f"{azl}{distancia/100}{fim}hm\n"
      f"{azl}{distancia/10}{fim}dam\n"
      f"{azl}{distancia*10}{fim}dm\n"
      f"{azl}{distancia*100}{fim}cm\n"
      f"{azl}{distancia*1000}{fim}mm\n")
