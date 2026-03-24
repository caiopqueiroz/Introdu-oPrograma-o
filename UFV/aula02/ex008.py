numero = int(input('Digite um número de 1 a 7: '))
if numero == 1:
    dia = 'domingo'
elif numero == 2:
    dia = 'segunda-feira'
elif numero == 3:
    dia = 'terça-feira'
elif numero == 4:
    dia = 'quarta-feira'
elif numero == 5:
    dia = 'quinta-feira'
elif numero == 6:
    dia = 'sexta-feira'
elif numero == 7:
    dia = 'sábado'
else:
    dia = 'inválido'
print(f'O dia da semana é {dia}')