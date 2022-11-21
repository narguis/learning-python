from utilidadesCEV.dado import dado
from utilidadesCEV.moeda import moeda

p = dado.leiaDinheiro("Digite o preço: R$")
a = dado.leiaTaxa("Taxa de aumento: ")
r = dado.leiaTaxa("Taxa de redução: ")
moeda.resumo(p, a, r)