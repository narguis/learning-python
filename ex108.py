from utilidadesCEV.moeda import moeda

preco = float(input("Digite o preço: R$"))

taxa = int(input("Qual é a porcentagem de desconto/aumento a ser calculado? "))

print(f"A metade de {moeda.real(preco)} é {moeda.real(moeda.metade(preco))}")
print(f"O dobro de {moeda.real(preco)} é {moeda.real(moeda.dobro(preco))}")
print(f"Com {taxa}% de desconto em {moeda.real(preco)}, o valor final é {moeda.real(moeda.diminuir(preco, taxa))}")
print(f"Com {taxa}% de aumento em {moeda.real(preco)}, o valor final é {moeda.real(moeda.aumentar(preco, taxa))}")