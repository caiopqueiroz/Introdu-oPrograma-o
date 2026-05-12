# cálculo de desconto


valor_total = int(input('Digite o valor total da compra: '))
if valor_total >= 500:
    desconto = 0.1 * valor_total
else:
    desconto = 0.05 * valor_total
valor_final = valor_total - desconto
print(f'Valor total da compra: R${valor_total:.2f}\nValor do desconto: R${desconto:.2f}\nValor final a ser pago: R${valor_final:.2f}')