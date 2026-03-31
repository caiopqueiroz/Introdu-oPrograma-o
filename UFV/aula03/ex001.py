# Faça um programa que solicite a velocidade máxima permitida em uma avenida e
# a velocidade com que o motorista estava dirigindo nela. Calcule e mostre a multa
# que uma pessoa vai receber, sabendo que são pagos: R$ 50 reais se o motorista
# ultrapassar em até 10km/h a velocidade permitida; R$ 100 reais, se o motorista
# ultrapassar de 11 a 30 km/h a velocidade permitida; e R$ 200 reais, se estiver acima
# de 31km/h da velocidade permitida.


v_max = int(input('Velocidade máxima na via (km/h): '))
velocidade = int(input('Velocidade do veículo (km/h): '))
frase_excesso = f'Excedeu a velocidade máxima em {velocidade - v_max} km/h'
excesso = velocidade - v_max
if 0 < excesso <= 10:
    print(f'{frase_excesso}. Multa de R$50,00')
elif 0 < excesso <= 30:
    print(f'{frase_excesso}. Multa de R$100,00')
elif 0 < excesso:
    print(f'{frase_excesso}. Multa de R$200,00')
else:
    print('Continue dirigindo com cuidado!')