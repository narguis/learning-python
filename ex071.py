valor = int(input("Qual valor você quer sacar? R$"))
cinquenta = vinte = dez = um = 0
while True:
    cinquenta = valor // 50
    valor -= cinquenta*50
    vinte = valor // 20
    valor -= vinte*20
    dez = valor // 10
    valor -= dez*10
    um = valor // 1
    valor -= um
    if cinquenta != 0:
        print(f'Total de {cinquenta:.0f} cédulas de R$50.')
    if vinte != 0:
        print(f'Total de {vinte:.0f} cédulas de R$20.')
    if dez != 0:
        print(f'Total de {dez:.0f} cédulas de R$10.')
    if um != 0:
        print(f'Total de {um:.0f} cédulas de R$1.')
    if valor == 0:
        break
