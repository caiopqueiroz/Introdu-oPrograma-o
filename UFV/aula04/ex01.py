from random import randint


def adivinhar_numero(numero):
    jogador = int(input('Digite um número de 0 a 100: '))
    print()
    if jogador > numero:
        print('Tente um valor mais baixo.')
        adivinhar_numero(numero)
    elif numero > jogador:
        print('Tente um valor mais alto.')
        adivinhar_numero(numero)
    else:
        print('Parabéns! Você acertou o número que eu estava pensando.')


numero = randint(0, 100)
adivinhar_numero(numero)