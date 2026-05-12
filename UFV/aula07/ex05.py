# simular a fase de grupos da copa do mundo


quantidade_selecoes_grupo = int(input('Quantidade de seleções participantes do grupo: '))
selecoes = list()
total_gols_marcados = 0
numero_selecoes_sem_derrota = 0
for time in range(0, quantidade_selecoes_grupo):
    nome = str(input('Nome da seleção: ')).strip().title()
    jogos = int(input('Quantidade de jogos disputados: '))
    vitorias = int(input('Quantidade de vitórias: '))
    empates = int(input('Quantidade de empates: '))
    derrotas = int(input('Quantidade de derrotas: '))
    gols_marcados = int(input('Quantidade de gols marcados: '))
    gols_sofridos = int(input('Quantidade de gols sofridos: '))

    saldo_gols = gols_marcados - gols_sofridos
    acrescimo_vitoria = 3 * vitorias
    acrescimo_empate = empates
    pontos = acrescimo_vitoria + acrescimo_empate
    
    selecao = list()
    selecao.append(nome)
    selecao.append(jogos)
    selecao.append(vitorias)
    selecao.append(empates)
    selecao.append(derrotas)
    selecao.append(gols_marcados)
    selecao.append(gols_sofridos)
    selecao.append(saldo_gols)
    selecao.append(pontos)
    selecoes.append(selecao[:])

    if time == 0:
        maior_selecao = nome
        mais_pontos = pontos
        selecao_melhor_saldo = nome
        melhor_saldo = saldo_gols
    else:
        if pontos > mais_pontos:
            maior_selecao = nome
        if saldo_gols > melhor_saldo:
            selecao_melhor_saldo = nome

    total_gols_marcados += gols_marcados

    if derrotas == 0:
        numero_selecoes_sem_derrota += 1

print()
for selecao in selecoes:
    print(selecao)
print('Seleção com mais pontos: ', maior_selecao)
print('Seleção com melhor saldo: ', selecao_melhor_saldo)
print('Média de gols por seleção: ', total_gols_marcados / quantidade_selecoes_grupo)
print('Número de seleções que não perderam nenhum jogo: ', numero_selecoes_sem_derrota)