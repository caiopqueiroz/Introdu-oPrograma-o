numeros = list()
for contador in range (0, 5):
    numeros.append(int(input(f'{contador + 1}º número: ')))
media = sum(numeros) / len(numeros)
print(f'A média desses valores vale {media}')
contador = 0
for numero in numeros:
    if numero > media:
        print(numero, end='  ')
        contador += 1
print(f'- {contador} números acima da média') 
