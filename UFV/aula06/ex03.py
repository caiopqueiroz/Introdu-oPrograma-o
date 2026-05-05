contador = 1
while contador <= 15:
    temperatura = float(input('Temperatura: '))
    if temperatura < 72:
        print(f'Temperatura muito baixa no minuto {contador}. Processo interrompido.')
        break
    if temperatura > 75:
        print(f'Temperatura muito alta no minuto {contador}. Processo interrompido.')
        break
    print(f'Minuto {contador}: Temperatura OK')
    contador += 1
if contador == 16:
    print('Pasteurização concluída com sucesso. Leite próprio para o consumo.')