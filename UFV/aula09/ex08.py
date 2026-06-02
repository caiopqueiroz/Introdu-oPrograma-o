from random import randint


vetor_x = list()
vetor_y = list()
vetor_z = list()
for contador in range(0, 20):
    vetor_x.append(randint(0, 10))
    vetor_y.append(randint(0, 10))
for contador in range(0, 20):
    vetor_z.append(vetor_x[contador] + vetor_y[contador])
print(f'\n{vetor_x}')
print(f'\n{vetor_y}')
print(f'\n{vetor_z}')