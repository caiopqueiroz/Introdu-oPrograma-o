from random import randint

soma_valores = 0
vetor = list()
matriz = list()
for linha in range(0, 3):
    for coluna in range(0, 6):
        vetor.append(int(input(f'Valor para a posição: ({linha}, {coluna}): ')))
    matriz.append(vetor[:])
    soma_valores += sum(vetor)
    vetor.clear()
    print()
for linha in matriz:
    print(linha)
print(f'\nA soma de todos os valores da matriz é: {soma_valores}')