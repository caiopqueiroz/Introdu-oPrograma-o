# Faça um programa para calcular o valor da área das seguintes figuras geométricas: retângulo, triângulo e circunferência. Para isso, você deve pedir ao usuário que digite os valores necessários para cada um dos cálculos. Para facilitar, pense em cada cálculo de forma separada. Faça um após o outro. Não se esqueça de mostrar os resultados na tela.
# Relembrando:
# Área do retângulo = Base x Altura;
# Área do triângulo = (Base x Altura)/2;
# Área da circunferência = π x Raio2
# Obs.: Por enquanto, utilize π = 3,1415


print('Calculadora da Área de Retângulo')
base_r = float(input('Base: '))
altura_r = float(input('Altura: '))
print(f'A área do retângulo vale {base_r * altura_r}')
print()

print('Calculadora da Área de Triângulo')
base_t = float(input('Base: '))
altura_t = float(input('Altura: '))
print(f'A área do triângulo vale {(base_t * altura_t) / 2}')
print()

print('Calculadora da Área de Círculo')
raio = float(input('Raio: '))
print(f'A área do círculo vale {3.1415 * (raio**2)}')