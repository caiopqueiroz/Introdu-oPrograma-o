numero1 = float(input('1º valor: '))
numero2 = float(input('2º valor: '))
operacao = str(input('Qual será a operação entre eles? (+ - * /) '))
if operacao == '+':
    print(f'{numero1} + {numero2} = {numero1 + numero2}')
elif operacao == '-':
    print(f'{numero1} - {numero2} = {numero1 - numero2}')
elif operacao == '*':
    print(f'{numero1} * {numero2} = {numero1 * numero2}')
elif operacao == '/':
    print(f'{numero1} / {numero2} = {numero1 / numero2}')