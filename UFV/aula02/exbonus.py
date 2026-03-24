notas = list()
for contador in range (0, 3):
    notas.append(float(input(f'Nota {contador + 1}: ')))
media = (notas[0] * 2 + notas[1] * 3 + notas[2] * 5) / 10 
if media >= 60:
    print(f'Média: {media} Aprovado!')
    if 60 <= media < 70:
        conceito = 'D'
    elif 70 <= media < 80:
        conceito = 'C'
    elif 80 <= media < 90:
        conceito = 'B'
    else: 
        conceito = 'A'
    print(f'Conceito {conceito}')
else:
    print(f'Média: {media} Reprovado')