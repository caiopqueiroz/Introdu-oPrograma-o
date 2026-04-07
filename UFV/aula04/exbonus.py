from random import randint


print('Jogo Batalha de Elementos')
print()
print('Escolha sua jogada:\n1) Fogo\n2) Água \n3) Planta\n4) Raio\n5) Pedra')
jogador1 = int(input('Número da sua escolha: '))
jogador2 = randint(1, 5)
vitoria = 'Você venceu!'
derrota = 'Você perdeu.'
print()
print(f'Eu escolhi o elemento {jogador2}')
print()
print('Resultado: ', end='')

if jogador1 == jogador2:
    print('Empate.')

elif jogador1 == 1:
    if jogador2 == 3 or jogador2 == 5:
        print(vitoria)
    else:
        print(derrota)

elif jogador1 == 2:
    if jogador2 == 1 or jogador2 == 5:
        print(vitoria)
    else:
        print(derrota)

elif jogador1 == 3:
    if jogador2 == 2 or jogador2 == 4:
        print(vitoria)
    else:
        print(derrota)
    
elif jogador1 == 4:
    if jogador2 == 2 or jogador2 == 1:
        print(vitoria)
    else:
        print(derrota)

else:
    if jogador2 == 4 or jogador2 == 3:
        print(vitoria)
    else:
        print(derrota)