# Calculates how much one will pay for a trip

dist = int(input("Qual é a distância da viagem em km? "))
print(f'A viagem custára R${dist*0.5}') if dist <= 200 else print(f'A viagem custará R${dist*0.45}')
