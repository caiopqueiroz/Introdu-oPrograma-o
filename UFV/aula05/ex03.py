numero = int(input('Digite um número: '))
contador = 1
print(f'--- Tabuada de {numero} ---')
print()
while contador <= numero:
    print(f'{contador} x {numero} = {numero * contador}')
    contador += 1 