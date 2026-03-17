# Faça um programa para calcular o valor da área das seguintes figuras geométricas: retângulo, triângulo e circunferência. Para isso, você deve pedir ao usuário que digite os valores necessários para cada um dos cálculos. Para facilitar, pense em cada cálculo de forma separada. Faça um após o outro. Não se esqueça de mostrar os resultados na tela.
# Relembrando:
# Área do retângulo = Base x Altura;
# Área do triângulo = (Base x Altura)/2;
# Área da circunferência = π x Raio2
# Obs.: Por enquanto, utilize π = 3,1415


class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    
    def area(self):
        return self.base * self.altura 
    

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura


    def area(self):
        return (self.base * self.altura) / 2
        
    
class Circulo:
    def __init__(self, raio):
        self.raio = raio


    def area(self):
        return 3.1415 * (self.raio**2)


forma1 = Retangulo(5, 5)
forma2 = Triangulo(5, 5)
forma3 = Circulo(5)
print(forma1.area())
print(forma2.area())
print(forma3.area())