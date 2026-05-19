from math import pow
from math import sqrt


cateto1 = float(input('Medida do cateto do triângulo retângulo: '))
cateto2 = float(input('Medida do outro cateto do triângulo retângulo: '))
hipotenusa = sqrt(pow(cateto1, 2) + pow(cateto2, 2))
print(f'A hipotenusa vale: {hipotenusa:.2f}')