from math import sqrt


print('Calculadora de Equação do 2º Grau')
a = float(input('Valor a: '))
b = float(input('Valor b: '))
c = float(input('Valor c: '))
delta = (b**2) - (4 * a * c)
if delta > 0:
    try:
        resultado = list()
        resultado.append((-b + sqrt(delta)) / (2 * a))
        resultado.append((-b - sqrt(delta)) / (2 * a))
    except:
        print('ERRO! Valor "a" não pode ser zero')
        resultado = list()
        resultado.append(0)
        resultado.append(0)
elif delta == 0: 
    resultado = -b / (2 * a) 
print(f'O delta vale {delta:.2f}')
if delta > 0:
    print(f'Solução: ({resultado[0]:.2f}, {resultado[1]:.2f})')
elif delta == 0:
    print(f'Solução: ({resultado:.2f})')
else: 
    print('Não há solução.')