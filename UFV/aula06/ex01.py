nomes = list()
valores = list()
quantidade_produtos = int(input('Quantos produtos diferentes? '))
contador = 0
while contador < quantidade_produtos:
    contador += 1
    nome = str(input('Nome: ')).strip().title()
    valor = float(input('Valor: '))
    quantidade = int(input('Quantidade: '))
    nomes.append(nome)
    valores.append(valor * quantidade)
contador = 0 
while contador < len(nomes):
    print(nomes[contador], valores[contador])
    contador += 1
print(f'Total {sum(valores)}')