from random import randint


matriz = list()
for linha in range(4):
    vetor = list()
    for coluna in range(5):
        vetor.append(randint(0, 9))
    matriz.append(vetor[:])
for linha in matriz:
    print(linha)
valor = int(input('\nDigite um número inteiro: '))
contido = False
contador_linha = -1
contador_coluna = -1
posicoes_elemento = list()
for linha in matriz:
    contador_linha += 1
    for elemento in linha:
        contador_coluna += 1
        if elemento == valor:
            contido = True
            posicoes_elemento.append(f'({contador_linha},{contador_coluna})')
    contador_coluna = -1
if contido:
    print(f'\nO número {valor} está na matriz na posição:')
    for posicao in posicoes_elemento:
        print(posicao, end=' ')
else:
    print(f'\nO número {valor} não está contido na matriz')
