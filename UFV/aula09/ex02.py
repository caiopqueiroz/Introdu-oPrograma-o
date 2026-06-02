vetor = list()
for contador in range(0, 5):
    vetor.append(float(input('Digite um valor: ')))
print('\nExibindo apenas os valores positivos:')
for numero in vetor:
    if numero > 0:
        print(numero)