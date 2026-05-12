# simular as estatísticas de uma partida de futebol

quantidade_jogadores_A = int(input('Quantidade de jogadores que participaram pelo time A: '))
quantidade_jogadores_B = int(input('Quantidade de jogadores que participaram pelo time B: '))
total_gols_A = 0
total_gols_B = 0
total_faltas_A = 0
total_faltas_B = 0

print('Time A')
for jogador in range(0, quantidade_jogadores_A):
    gols_marcados = int(input('Quantidade de gols marcados: '))
    faltas_cometidas = int(input('Quantidade de faltas cometidas: '))

    total_gols_A += gols_marcados 

    total_faltas_A += faltas_cometidas

    if jogador == 0:
        artilheiro_A = gols_marcados
    else:
        if gols_marcados > artilheiro_A:
            artilheiro_A = gols_marcados

print('Time B')
for jogador in range(0, quantidade_jogadores_B):
    gols_marcados = int(input('Quantidade de gols marcados: '))
    faltas_cometidas = int(input('Quantidade de faltas cometidas: '))

    total_gols_B += gols_marcados

    total_faltas_B += faltas_cometidas

    if jogador == 0:
        artilheiro_B = gols_marcados
    else:
        if gols_marcados > artilheiro_B:
            artilheiro_B = gols_marcados

print()
print('Total de gols do time A: ', total_gols_A)
print('Total de gols do time B: ', total_gols_B)
print('Total de faltas do time A: ', total_faltas_A)
print('Total de faltas do time B: ', total_faltas_B)
if total_gols_A > total_gols_B:
    print('O time A venceu')
elif total_gols_B > total_gols_A:
    print('O time B venceu')
else: 
    print('Empate')
if artilheiro_A > artilheiro_B:
    print(f'O artilheiro foi do time A e marcou {artilheiro_A} gols')
elif artilheiro_B > artilheiro_A:
    print(f'O artilheiro foi do time B e marcou {artilheiro_B} gols')