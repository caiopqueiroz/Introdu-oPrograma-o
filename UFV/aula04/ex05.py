from random import randint
from time import sleep


jogador1 = str(input('Nome do jogador 1: '))
jogador2 = str(input('Nome do jogador 2: '))
jogador3 = str(input('Nome do jogador 3: '))
passos1 = 0
passos2 = 0
passos3 = 0 
rodada = 1
vencedor = ''
passos = list()
while passos1 < 30 and passos2 < 30 and passos3 < 30:
    print()
    print(f'Rodada {rodada}. Avançando passos aleatoriamente: ')
    print()
    avanco1 = randint(1, 5)
    avanco2 = randint(1, 5)
    avanco3 = randint(1, 5)
    passos1 += avanco1
    passos2 += avanco2
    passos3 += avanco3
    print(f'{jogador1} avançou {avanco1} passos, totalizando {passos1}\n{jogador2} avançou {avanco2} passos, totalizando {passos2}\n{jogador3} avançou {avanco3} passos, totalizando {passos3}')
    print()
    print('Fim da rodada.')
    rodada += 1 
    sleep(2)
passos.append(passos1)
passos.append(passos2)
passos.append(passos3)
if passos1 == passos2 or passos1 == passos3 or passos2 == passos3:
    print('Empate.')
else: 
    if max(passos) == passos1:
        vencedor = jogador1
    elif max(passos) == passos2:
        vencedor = jogador2
    else:
        vencedor = jogador3
    print()
    print(f'\033[1;32mO vencedor foi {vencedor}. Parabéns!\033[m')