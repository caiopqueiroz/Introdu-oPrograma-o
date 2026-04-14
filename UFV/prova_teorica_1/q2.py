# temperatura
temperatura = int(input('Temperatura interna do equipamento: '))
if temperatura < 0:
    mensagem = 'RISCO DE CONGELAMENTO'
elif temperatura <= 70:
    mensagem = 'Temperatura normal'
elif temperatura <= 100:
    mensagem = 'Temperatura elevada'
else:
    mensagem = 'RISCO DE INCÊNDIO'
print(mensagem) 