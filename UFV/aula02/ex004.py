numeros = list()
for contador in range (0, 3):
    numeros.append(int(input(f'Lado {contador + 1}: ')))
if numeros[0] < numeros[1] + numeros[2] and numeros[1] < numeros[0] + numeros [2] and numeros[2] < numeros[0] + numeros[1]:
    print('Esses 3 valores podem formar um triângulo')
else:
    print('Esses 3 valores NÃO podem formar um triângulo')