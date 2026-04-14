from time import sleep
from random import randint


print('Gerando número aleatório...')
numero = randint(1, 100)
if numero <= 30:
    premio = 'R$10.00'
elif numero <= 70:
    premio = 'R$50.00'
else:
    premio = 'R$100.00'
sleep(2)
print(f'O número sorteado foi {numero}\nParabéns! Você ganhou o prêmio de {premio}')
