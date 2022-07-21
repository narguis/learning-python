# Receives detail of a product's payment and returns the final price

azul = '\033[34m'
verde = '\033[32m'
vermelho = '\033[31m'
fim = '\033[m'
# Asks if they'll pay in one lump sum or in installments
print(f'{azul}O valor total do produto é de {verde}R$250,00{fim}. Qual será a forma de pagamento?')
avpc = int(input(f'Digite {azul}1{fim} para pagar à vista e {azul}2{fim} para pagar parcelado: '))
# If they pay in one lump sum, will they pay by cash or card?
if avpc == 1:
    dc = int(input(f'Digite {azul}1{fim} para pagar no {verde}dinheiro{fim} e {azul}2{fim} para '
                   f'pagar {verde}à vista no cartão{fim}: '))
    if dc == 1:
        print(f'O valor total será de {verde}R$225,00{fim}.')
    elif dc == 2:
        print(f'O valor total será de {verde}R$237,50{fim}.')
    else:
        print(f'Digite {azul}1{fim} ou {azul}2{fim} para continuar!') and print(dc)
# If they choose to pay in parts, will it be in up to two parts or three parts or more
elif avpc == 2:
    dt = int(input(f'Digite {azul}1{fim} para parcelar em até {vermelho}2x{fim} e {azul}2{fim} '
                   f'para parcelar em {vermelho}3x{fim} ou mais: '))
    if dt == 1:
        print(f'O valor total será de {verde}R$250,00{fim}.')
    elif dt == 2:
        print(f'O valor total será de {verde}R$300,00{fim}.')
    else:
        print(f'Digite {azul}1{fim} ou {azul}2{fim} para continuar!') and print(dt)
else:
    print(f'Digite {azul}1{fim} ou {azul}2{fim} para continuar!') and print(avpc)
