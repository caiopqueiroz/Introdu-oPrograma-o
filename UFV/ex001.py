# Faça um programa para o cálculo da seguinte expressão: f(x) = Kx² + 2x + 5 O valor de x deve ser fornecido pelo usuário (use o comando input). Considere que K possui o valor 109. Não esqueça de mostrar o resultado na tela (use o comando print).


print('Calculadora da expressão f(x) = Kx² + 2x + 5')
x = float(input('Digite um valor pra x: '))
resultado = (109 * x**2) + (2 * x) + 5
print(f'f(x) vale {resultado:.2f}')