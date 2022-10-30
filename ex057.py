sexo = input('Sexo [M/F]: ').strip()
while sexo not in 'MmFf':
    sexo = input('Sexo inválido! Digite seu sexo [M/F]: ')
print(f"Sexo registrado como {sexo.upper()} com sucesso!")