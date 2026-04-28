# fim: matrúcula = 9999
alunos = list()
total_alunos = 0
total_aprovados = 0
total_reprovados = 0
while True:
    matricula = int(input('\nMatrícula: '))
    if matricula == 9999:
        break
    notas = list()
    for contador in range(0, 3):
        notas.append(int(input(f'Nota {contador + 1}: ')))
    media_final = (2 * notas[0]) + (3 * notas[1]) + (4 * notas[2]) / 9
    if media_final >= 60:
        situacao = 'APROVADO'
        total_aprovados += 1
    else:
        situacao = 'REPROVADO'
        total_reprovados += 1
    aluno = list()
    aluno.append(matricula)
    aluno.append(media_final)
    aluno.append(situacao)
    alunos.append(aluno[:])
    total_alunos += 1
print('\nPanorama geral:\n')
for aluno in alunos:
    print(f'{aluno[0]} - {aluno[1]:.2f} - {aluno[2]}')
print(f'\nTotal de alunos: {total_alunos}\nTotal de aprovados: {total_aprovados}\nTotal de reprovados: {total_reprovados}')
