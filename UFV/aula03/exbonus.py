for contador in range (0, 5):
    numero = int(input('Digite um número inteiro: '))
    if contador == 0:
        maior = numero
    else:
        if numero > maior:
            maior = numero
print(f'O maior valor digitado foi {maior}')
        