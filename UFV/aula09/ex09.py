from random import randint


vetor_a = list()
vetor_b = list()
vetor_c = list()
contador_a = 0
contador_b = 0
for contador in range(0, 5):
    vetor_a.append(randint(0, 10))
    vetor_b.append(randint(0, 10))
for contador in range(0, 10):
    if contador % 2 == 0:
        vetor_c.append(vetor_a[contador_a])
        contador_a += 1
    else:
        vetor_c.append(vetor_b[contador_b])
        contador_b += 1
print(vetor_a, vetor_b)
print(f'\n{vetor_c}')