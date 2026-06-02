alturas = list()
for atleta in range(0, 10):
    alturas.append(float(input(f'Digite a altura do atleta {atleta + 1}: (em metros) ' )))
media_alturas = sum(alturas) / len(alturas)
print(f'\nA média das alturas é {media_alturas:.2f}')
print('\nAlturas que estão acima da média:')
for altura in alturas:
    if altura > media_alturas:
        print(f'{altura} m')