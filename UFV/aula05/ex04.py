contador = 1
soma_salarios = 0
print('Digite 0 para interromper as entradas\n')
while True:
    salario = float(input('Salário do funcionário: '))
    if salario == 0:
        break
    nome = str(input('Nome do funcionário: ')).strip().title()
    print()
    soma_salarios += salario
    if contador == 1:
        maior_salario = salario
        nome_maior_salario = nome
        menor_salario = salario
        nome_menor_salario = nome
    else:
        if salario > maior_salario:
            maior_salario = salario
            nome_maior_salario = nome
        if salario < menor_salario:
            menor_salario = salario
            nome_menor_salario = nome
    contador += 1 
media_salarios = soma_salarios / (contador - 1)
print(f'\nA média dos salários é R${media_salarios:.2f}\n')
print(f'O maior salário é de {nome_maior_salario}: R${maior_salario:.2f}\n')
print(f'O menor salário é de {nome_menor_salario}: R${menor_salario:.2f}\n')