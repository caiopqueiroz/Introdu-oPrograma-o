notas = list()
quantidade_acima_media = 0
for nota in range(0, 3):
    notas.append(float(input(f'Digite a nota {nota + 1}: ')))
media = sum(notas) / len(notas)
for nota in notas:
    if nota > media:
        quantidade_acima_media += 1
print(f'\nA média da turma foi {media:.2f}\n{quantidade_acima_media} foi a quantidade de alunos que obtiveram notas acima da média')
