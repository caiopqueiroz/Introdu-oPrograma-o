# controle de vendas de uma pizzaria 


quantidade_pedidos = int(input('Quantidade de pedidos realizados no dia: '))
faturamento = 0
total_pizzas_vendidas = 0
quantidade_pedidos_altos = 0
for pedido in range(0, quantidade_pedidos):
    nome_cliente = str(input('Nome do cliente: ')).strip().title()
    sabor_pizza = str(input('Sabor da pizza: ')).strip().title()
    tamanho_pizza = str(input('Tamanho da pizza: (P, M ou G): ')).upper().strip()
    quantidade_pizzas = int(input('Quantidade de pizzas pedidas: '))
    valor_unitario = float(input('Valor unitário da pizza: '))

    valor_total_pedido = valor_unitario * quantidade_pizzas

    faturamento += valor_total_pedido

    if pedido == 0:
        maior_pedido = valor_total_pedido
    else:
        if valor_total_pedido > maior_pedido:
            maior_pedido = valor_total_pedido

    total_pizzas_vendidas += quantidade_pizzas

    if valor_total_pedido > 300:
        quantidade_pedidos_altos += 1

print()
print('Faturamento total: ', faturamento)
print('Preço do pedido mais caro: ', maior_pedido)
print('Total de pizzas vendidas: ', total_pizzas_vendidas)
print('Média de preço dos pedidos: ', faturamento / quantidade_pedidos)
print('Quantidade de pedidos acima de R$300,00: ', quantidade_pedidos_altos)
