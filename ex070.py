continuar = nomebarato = ''
mil = total = conta = maisbarato = 0
while True:
    produto = input('Nome do produto: ').strip()
    preco = int(input('Preço: R$'))
    continuar = input('Quer continuar?[S/N]: ').strip()[0]
    while continuar not in 'sSnN':
        continuar = input('Quer continuar?[S/N]: ').strip()[0]
    if continuar in 'nN':
        break
    conta += 1
    if conta == 1:
        maisbarato = preco
    elif preco < maisbarato:
        nomebarato = produto
        maisbarato = preco
    total += preco
    if preco > 1000:
        mil += 1
print(f'O valor total foi R${total}.\nVocê comprou {mil} produtos que custam mais de R$1000.')
print(f'O produto mais barato foi {nomebarato}, que custou R${maisbarato}.')
