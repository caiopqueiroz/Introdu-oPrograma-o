from math import sqrt

comando = 'S'
while comando == 'S':
    cidade1_x = int(input('\nCoordenada x da cidade 1: '))
    cidade1_y = int(input('Coordernada y da cidade 1: '))
    cidade2_x = int(input('Coordenada x da cidade 2: '))
    cidade2_y = int(input('Coordenada y da cidade 2: '))
    distancia = sqrt((cidade2_x - cidade1_x)**2 + (cidade2_y - cidade1_y)**2)
    print(f'Distância entre as cidades: {distancia:.2f} km')
    if distancia <= 50:
        tamanho = 'distância é curta'
    elif distancia <= 150:
        tamanho = 'distância é média'
    else:
        tamanho = 'distância é longa'
    print(f'A {tamanho}')
    comando = str(input('\nDeseja calcular outra distância? '))[0].strip().upper()
    if 'N' in comando:
        break
