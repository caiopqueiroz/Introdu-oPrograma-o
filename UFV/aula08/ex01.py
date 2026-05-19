from random import randint
from time import sleep


comando = 'S'
while comando == 'S':
    print('\nJogando dados...')
    sleep(2)
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    print(f'Dado 1: {dado1}\nDado 2: {dado2}')
    print(f'Soma dos dados: {dado1 + dado2}')
    if dado1 + dado2 == 7 or dado1 + dado2 == 11:
        print('Vitória!')
    else:
        print('Derrota')
    comando = str(input('\nDeseja jogar mais uma vez? (S/N): '))[0].strip().upper()
    if 'N' in comando:
        break