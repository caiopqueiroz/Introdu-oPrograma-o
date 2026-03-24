numero = int(input('Digite um número inteiro: '))
if numero > 0:
    valor = 'positivo'
elif numero == 0:
    valor = 'nulo'
else:
    valor = 'negativo'
print(f'O número digitado é {valor}')