identidade = True
matriz = list()
vetor = list()
for linha in range(0, 4):
    for coluna in range(0, 4):
        valor = int(input(f'Valor para a posição ({linha}, {coluna}): '))
        vetor.append(valor)
        if linha == coluna:
            if valor != 1:
                identidade = False
        else:
            if valor != 0:
                identidade = False
    matriz.append(vetor[:])
    vetor.clear()
    print()
for linha in matriz:
    print(linha)
if identidade:
    print('\nA matriz é identidade')
else:
    print('\nA matriz não é identidade')