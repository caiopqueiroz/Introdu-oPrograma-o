# cálculo de fatorial


numero = int(input('Número inteiro positivo: '))
fatorial = 1
for contador in range(numero, 0, -1):
    if contador == 1:
        print(contador, end =' = ')
    else:
        print(contador, end=' x ')
    fatorial *= contador
print(fatorial)