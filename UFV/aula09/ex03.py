vetor = list()
for numero in range(1, 21):
    if numero % 2 != 0:
        vetor.append(numero ** 2)
print('Quadrados dos número ímpares de 1 a 20:')
for numero in vetor:
    print(numero)