vetor_a = list()
print('Lista sem repetição de valores:')
for contador in range(0, 10):
    valor = float(input('Digite um valor numérico: '))
    while valor in vetor_a:
        print('Esse valor já foi digitado. Digite outro')
        valor = float(input('Digite um valor numérico: '))
    vetor_a.append(valor)

vetor_b = list()
print('\nLista com repetição de valores:')
for contador in range(0, 10):
    vetor_b.append(float(input('Digite um valor numérico: ')))

variavel = float(input('\nDigite um valor para a variável x: '))

existe = False
contador = 0
for valor in vetor_a:
    if valor == variavel:
        print(f'\nO vetor A possui a variável {variavel} na posição {contador}')
        posicao = contador
        existe = True
    contador += 1

if existe:
    print(f'\nO elemento do vetor B na posição {posicao} é {vetor_b[posicao]}')
else:
    print('\nA variável não existe no vetor A')
