nome = str(input('Atleta: ')).strip().title()
notas = list()
for contador in range(0, 7):
    notas.append(int(input(f'Nota {contador + 1}: ')))
soma_notas = sum(notas)
soma_notas -= max(notas) + min(notas)
media = soma_notas / 7
print('\nResultado final:')
print(f'Atleta: {nome}')
print(f'Melhor nota: {max(notas)}')
print(f'Pior nota: {min(notas)}')
print(f'Média: {media:.2f}')