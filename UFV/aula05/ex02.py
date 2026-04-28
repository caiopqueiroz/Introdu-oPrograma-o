numero = int(input('Digite um número: '))
fatorial = 1
print(f'{numero}! = ', end='')
while numero > 0:
    print(f'* {numero} ', end='')
    fatorial *= numero
    numero -= 1
print(f'= {fatorial}')