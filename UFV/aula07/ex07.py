# controle de gados em uma fazenda



quantidade_animais = int(input('Quantidade de animais cadastrados: '))
soma_peso = 0
soma_quantidade_leite = 0
soma_idades_altas = 0
for animal in range(0, quantidade_animais):
    numero = int(input('Número de identificação do gado: '))
    peso = int(input('Peso do animal em kg: '))
    idade = int(input('Idade do animal em anos: '))
    quantidade_leite = int(input('Quantidade de litros de leite produzidos por dia (0 caso não produza leite) '))

    soma_peso += peso
    
    if animal == 0:
        maior_peso = peso
        menor_peso = peso
        numero_maior_produtor = numero
        maior_quantidade_leite = quantidade_leite
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
        if quantidade_leite > maior_quantidade_leite:
            numero_maior_produtor = numero

    soma_quantidade_leite += quantidade_leite 

    if idade > 5:
        soma_idades_altas += 1

print()
print('Quantidade de animais: ', quantidade_animais)
print('Média de peso: ', soma_peso / quantidade_animais)
print('Maior peso: ', maior_peso)
print('Menor peso: ', menor_peso)
print('Soma da quantidade de leite: ', soma_quantidade_leite)
print('Quantidade de animais com idade > 5: ', soma_idades_altas)
print('Número do animal que mais produz leite: ', numero_maior_produtor)
