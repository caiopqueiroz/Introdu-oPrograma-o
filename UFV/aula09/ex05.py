vetor = list()
for contador in range(0, 5):
    vetor.append(float(input('Digite um valor: ')))
print(f'\n{vetor}')
print('\nTrocando de lugar o primeiro elemento e o último:')
primeiro_elemento = vetor[0]
vetor[0] = vetor[4]
vetor[4] = primeiro_elemento
print(f'\n{vetor}')