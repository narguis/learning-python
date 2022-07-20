# Converting degrees to radians and calculating its sin, cosine and tangent

import math
ang = int(input("Digite um ângulo: "))
radian = math.radians(ang)
print(f"O ângulo de {ang} tem o seno de {math.sin(radian):.2f}\n"
      f"O cosseno de {math.cos(radian):.2f}\n"
      f"E a tangente de {math.tan(radian):.2f}")
