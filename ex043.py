# Calculates one Body Mass Index (BMI) and says if they're underweight, morbidly obese
# or something in between

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso/(pow(altura, 2))
msg = 'Você está'
if imc < 18.5:
    print(f'{msg} ABAIXO DO PESO!')
elif imc < 25:
    print(f'{msg} no PESO IDEAL!')
elif imc < 30:
    print(f'{msg} com SOBREPESO!')
elif imc < 40:
    print(f'{msg} OBESO!')
else:
    print(f'{msg} em OBESIDADE MÓRBIDA!')
