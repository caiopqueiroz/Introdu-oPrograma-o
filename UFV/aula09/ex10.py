temperaturas = list()
for dia in range(0, 10):
    temperaturas.append(float(input(f'Digite a temperatura do dia {dia + 1}: ')))
    while temperaturas[dia] > 40 or temperaturas[dia] < 15:
        print('Temperatura inválida')
        temperaturas.pop()
        temperaturas.append(float(input(f'Digite a temperatura do dia {dia + 1}: ')))
print(f'\nA menor temperatura foi {min(temperaturas)}\nA maior temperatura foi {max(temperaturas)}')