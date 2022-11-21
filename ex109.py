from utilidadesCEV.moeda import moeda

preco = float(input("Digite o preço: R$"))

taxa = int(input("Qual é a porcentagem de desconto/aumento a ser calculado? "))

print(f"A metade de {moeda.real(preco)} é {moeda.metade(preco, True)}")
print(f"O dobro de {moeda.real(preco)} é {moeda.dobro(preco, True)}")
print(f"Com {taxa}% de desconto em {moeda.real(preco)}, o valor final é {moeda.diminuir(preco, taxa, True)}")
print(f"Com {taxa}% de aumento em {moeda.real(preco)}, o valor final é {moeda.aumentar(preco, taxa, True)}")
