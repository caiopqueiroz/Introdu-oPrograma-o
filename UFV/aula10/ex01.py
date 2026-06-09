matriz = list()
for linha in range(3):
    vetor = list()
    for coluna in range(3):
        vetor.append(int(input(f'Valor para a posição ({linha}, {coluna}): ')))
    matriz.append(vetor[:])
    print()
for linha in matriz:
    print(linha)
nula = True
for linha in matriz:
    for elemento in linha:
        if elemento != 0:
            nula = False
if nula:
    print('\nA matriz é nula')
else:
    print('\nA matriz não é nula')