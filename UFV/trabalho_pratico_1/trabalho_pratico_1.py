# regras:
# não usar estruturas de repetição

# execução do programa:
# escolher jogar ou sair 
# ler o nome do jogador
# selecionar dificuldade (fácil, médio ou difícil)
# responder 10 perguntas de múltipla escolha (alternativas a, b, c)
# exibir mensagem de acerto ou de erro
# somar 10 pontos a cada questão acertada
# final: exibir total de pontos 


print('Bem-vindo(a) ao Quiz com Níveis de Dificuldade')
print()
print('Escolha uma das opções abaixo:\n(1) Jogar\n(2) Sair')
comando1 = int(input('Opção: '))
if comando1 == 1:
    pontos = 0 
    acerto = '\033[1;32mResposta correta! +10 pontos!\033[m'
    erro = '\033[1;31mResposta errada.\033[m'
    print()
    nome = str(input('Informe seu nome: '))
    print()
    print('Escolha seu nível:\n(1) Fácil\n(2) Médio\n(3) Difícil')
    nivel = int(input('Opção: '))
    if nivel == 1:
        print()
        print('Pergunta 1: Qual é a capital do Brasil?\na) Rio de Janeiro\nb) Brasília\nc) São Paulo')
        resposta = str(input('Resposta: ')).lower()
        if 'b' in resposta:
            pontos += 10
            print(acerto)
        else:
            print(erro)

        print()
        print('Pergunta 2: Quantos dias tem um ano comum?\na) 366\nb) 364\nc) 365')
        resposta = str(input('Resposta: ')).lower()
        if 'c' in resposta:
            pontos += 10
            print(acerto)
        else:
            print(erro)

        print()
        print('Pergunta 3: Qual o maior planeta do sistema solar?\na) Terra\nb) Júpiter\nc) Saturno')
        resposta = str(input('Resposta: ')).lower()
        if 'b' in resposta:
            pontos += 10
            print(acerto)
        else: 
            print(erro)
        
        print()
        print('Pergunta 4: Quem descobriu o Brasil?\na) Cristóvão Colombo\nb) Pedro Álvares Cabral\nc) Vasco da Gama')
        resposta = str(input('Resposta: ')).lower()
        if 'b' in resposta:
            pontos += 10
            print(acerto)
        else:
            print(erro)

        print()
        print('Pergunta 5: Qual é a cor do céu em um dia claro?\na) Azul\nb) Verde\nc) Vermelho')
        resposta = str(input('Resposta: ')).lower()
        if 'a' in resposta:
            pontos += 10
            print(acerto)
        else:
            print(erro)
    if nivel == 2:
        pass
    if nivel == 3:
        pass
    print()
    print(f'Fim de jogo, {nome}. Sua pontuação final: {pontos} pontos. Parabéns!')
if comando1 == 2:
    print()
    print('Programa Encerrado')


