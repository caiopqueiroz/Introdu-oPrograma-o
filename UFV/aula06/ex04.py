hp_guerreiro = 100
hp_dragao = 150
dano_guerreiro = 20
dano_dragao = 15
print(f'Hp do Guerreiro: {hp_guerreiro}\nHp do Dragão: {hp_dragao}')
while hp_guerreiro > 0 and hp_dragao > 0:
    opcao = 0
    while opcao != 1 and opcao != 2:
        print('\nOpção 1: Atacar\nOpção 2: Defender')
        opcao = int(input('Escolha: '))
    if opcao == 1:
        hp_guerreiro -= dano_dragao
        hp_dragao -= dano_guerreiro
    if opcao == 2:
        hp_guerreiro -= dano_dragao // 2
    print(f'\nHp do Guerreiro: {hp_guerreiro}\nHp do Dragão: {hp_dragao}')
if hp_guerreiro > 0:
    print('\nVitória! O dragão foi derrotado e o tesouro é seu.')
if hp_dragao > 0:
    print('\nGame over! Você foi derrotado pelo Dragão.')
    
        