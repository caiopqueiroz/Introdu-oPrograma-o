quantidade_alunos = int(input('Quantidade de alunos da turma: '))
soma_notas = 0
for aluno in range(0, quantidade_alunos):
    nota = float(input(f'Nota do aluno {aluno + 1}: '))

    soma_notas += nota

    if aluno == 0:
        maior_nota = nota
        menor_nota = nota
    else:
        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota

print()
print('Média das notas da turma: ', soma_notas / quantidade_alunos)
print('Maior nota: ', maior_nota)
print('Menor nota: ', menor_nota)