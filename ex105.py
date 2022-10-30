def notas(*n, sit = False):
    """
    :param n: Recebe uma quantidade ilimitada de notas
    :param sit: Mostra a situação da turma (opcional)
    :return: Dicionário com o Total de notas, a maior e a menor nota e a média entre elas
    """
    s = i = 0
    lista = sorted(n)
    dic = {}
    for i in lista:
        s += i
    dic['Total'] = len(lista)
    dic['Maior'] = max(lista)
    dic['Menor'] = min(lista)
    dic['Média'] = s / dic['Total']
    if dic['Média'] < 5:
        dic['Situação'] = 'RUIM'
    elif dic['Média'] < 7:
        dic['Situação'] = 'RAZOÁVEL'
    else:
        dic['Situação'] = 'BOA'
    if sit is False:
        del dic['Situação']
    return dic

resp = (notas(8, 9, 7, sit=True))
print(resp)
help(notas)