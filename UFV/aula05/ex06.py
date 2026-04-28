comando = 'S'
total = 0
while True:
    comando = str(input('\nLer mais um item? (S/N) '))[0].strip().upper()
    if comando != 'S':
        break
    codigo = int(input('\nCódigo: '))
    quantidade = int(input('Quantidade: '))
    if codigo == 100:
        preco = 11.2
    elif codigo == 101:
        preco = 15.3
    elif codigo == 102:
        preco = 17.5
    elif codigo == 103:
        preco = 20.2
    elif codigo == 104:
        preco = 21.3
    elif codigo == 105:
        preco = 7
    valor = preco * quantidade
    total += valor
    print(f'Valor: {valor:.2f}')
print(f'\nTotal do pedido: R${total:.2f}')


    
