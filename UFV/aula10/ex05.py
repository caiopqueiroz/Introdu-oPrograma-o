from random import randint


n = int(input('Quantidade de linhas da matriz: '))
m = int(input('Quantidade de colunas da matriz: '))
matriz = list()
for linha in range(0, n):
    vetor = list()
    for coluna in range(0, m):
        vetor.append(randint(0, 9))
    matriz.append(vetor[:])
print()
for linha in matriz:
    print(linha)
