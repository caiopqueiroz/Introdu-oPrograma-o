altura = float(input('Altura da pessoa: (m) '))
sexo = str(input('Sexo da pessoa: ')).upper()
if 'M' in sexo[0]:
    peso_ideal = 72.7 * altura - 58
elif 'F' in sexo[0]:
    peso_ideal = 62.1 * altura - 44.7
print(f'O seu peso ideal é {peso_ideal:.2f} kg')