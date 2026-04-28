# sem usar lista
contador = 1
soma_idades = 0
while contador <= 5:
    idade = int(input(f'{contador}ª idade: '))
    soma_idades += idade
    contador += 1
media = soma_idades / (contador - 1)
print(f'A média das idades é {media:.2f}')

# usando lista
idades = list()
for contador in range(1, 6):
    idades.append(int(input(f'{contador}ª idade: ')))
media = sum(idades) / 5
print(f'A média das idades é {media:.2f}')