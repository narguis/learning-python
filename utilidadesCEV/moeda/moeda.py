def aumentar(i, t, fm=False):
    n = i * (t/100)
    if fm is True:
        return (f"R${i+n:.2f}")
    else:
        return i+n

def diminuir(i, t, fm=False):
    n = i* (t/100)
    if fm is True:
        return (f"R${i-n:.2f}")
    else:
        return i-n

def dobro(i, fm=False):
    if fm is True:
        return (f"R${i*2:.2f}")
    else:
        return i*2

def metade(i, fm=False):
    if fm is True:
        return (f"R${i/2:.2f}")
    else:
        return i/2

def real(i):
    r = (f"R${i:.2f}")
    return r

def resumo(i, aum, red):
    print("-" * 30)
    print(f"{'RESUMO DO VALOR':^30}")
    print("-" * 30)
    print(f"{'Preço analisado:':<20}", end='')
    print(f"R${i:.2f}")
    print(f"{'Dobro do preço:':<20}", end='')
    print(dobro(i, True))
    print(f"{'Metade do preço:':<20}", end='')
    print(metade(i, True))
    print(f"{f'{aum}% de aumento:':<20}", end='')
    print(aumentar(i, aum, True))
    print(f"{f'{red}% de redução:':<20}", end='')
    print(diminuir(i, red, True))
    print("-" * 30)

    
