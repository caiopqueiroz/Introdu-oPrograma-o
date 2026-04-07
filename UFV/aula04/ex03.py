from random import choice


opcoes = ['cara', 'coroa']
resultados = list()
contador_cara = 0
contador_coroa = 0
for contador in range(0, 5):
    resultado = choice(opcoes)
    resultados.append(resultado)
    if resultado == 'cara':
        contador_cara += 1
    else:
        contador_coroa += 1
print('Simulando 5 lançamentos de moeda:')    
print(resultados)
print(f'Total de caras: {contador_cara}\nTotal de coroas: {contador_coroa}')