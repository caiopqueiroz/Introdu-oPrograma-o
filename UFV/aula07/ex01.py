numero = int(input('Número inteiro positivo: '))
somatorio = 0
for contador in range(1, numero + 1):
    if contador % 2 != 0:
        somatorio += contador
print(f'Soma dos números ímpares de 1 a {numero}: {somatorio}')