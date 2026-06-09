from random import randint


matriz = list()
for linha in range(5):
    vetor = list()
    for coluna in range(5):
        if linha == coluna:
            vetor.append(randint(0, 9))
        else:
            vetor.append('')
    matriz.append(vetor[:])
for linha in matriz:
    print(linha)