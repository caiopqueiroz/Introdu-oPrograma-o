numeros = list()
for contador in range (0, 4):
    numeros.append(int(input(f'{contador + 1}º número: ')))
somaPares = 0
for numero in numeros:
    if numero % 2 == 0:
        somaPares += numero
print(f'A soma dos números pares digitados vale {somaPares}')