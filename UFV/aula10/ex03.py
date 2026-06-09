multiplicador = int(input('Digite um número inteiro: '))
matriz = list()
for linha in range(10):
    vetor = list()
    for coluna in range(3):
        if coluna == 0:
            vetor.append(multiplicador)
        elif coluna == 1:
            vetor.append(linha + 1)
        else:
            vetor.append(multiplicador * (linha + 1))
    matriz.append(vetor[:])
print()
print(f'Matriz tabuada do {multiplicador}: ')
for linha in matriz:
    print(linha)