temperatura = 0
contador = 0
while temperatura < 75:
    aumento = 0
    while aumento <= 0:
        aumento = float(input('Aumento: '))
        if aumento <= 0:
            print('Aumento inválido')
    temperatura += aumento
    contador += 1
print(f'Temperatura final: {temperatura}°\nQuantidade de ciclos: {contador}\nProcesso concluído')
if temperatura > 75:
    excesso = temperatura - 75
    print(f'A temperatura ultrpassou o valor ideal em {excesso:.2f}°')