# Gets a students grades and states if they failed, passed or are able to try
# a retake test

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
med = (n1+n2)/2
if med < 5:
    print('\033[31mVocê foi REPROVADO!\033[m')
elif med < 7:
    print('\033[33mVocê está DE RECUPERAÇÃO!\033[m')
else:
    print('\033[32mVocê foi APROVADO!\033[m')
