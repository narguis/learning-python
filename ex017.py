# Calculating the hypotenuse of a triangle

from math import hypot
co = float(input("\033[1;31mComprimento do Cateto Oposto:\033[m "))
ca = float(input("\033[1;34mComprimento do Cateto Adjacente:\033[m "))
print(f"\033[30;107mA hipotenusa vale\033[m \033[35m{hypot(co,ca):.2f}\033[m")
