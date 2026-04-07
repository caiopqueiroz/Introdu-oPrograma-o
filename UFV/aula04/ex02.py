from random import choice


nomes = list()
for contador in range(0, 5):
    nomes.append(str(input(f'Digite o {contador + 1}º nome: ')))
print(f'O vencedor é: {choice(nomes)}')