# Caio Queiroz - Matrícula 7466
# Pedro Hashimoto - Matrícula 7467

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
        resposta = str(input('Resposta: ')).lower().strip()
        if 'b' in resposta:
            pontos += 10
            print(acerto)
        else:
            print(erro)

        print()
        print('Pergunta 2: Quantos dias tem um ano comum?\na) 366\nb) 364\nc) 365')
        resposta = str(input('Resposta: ')).lower().strip()
        if 'c' in resposta:
            pontos += 10
            print(acerto)
        else:
            print(erro)

        print()
        print('Pergunta 3: Qual o maior planeta do sistema solar?\na) Terra\nb) Júpiter\nc) Saturno')
        resposta = str(input('Resposta: ')).lower().strip()
        if 'b' in resposta:
            pontos += 10
            print(acerto)
        else:
            print(erro)

        print()
        print('Pergunta 4: Quem descobriu o Brasil?\na) Cristóvão Colombo\nb) Pedro Álvares Cabral\nc) Vasco da Gama')
        resposta = str(input('Resposta: ')).lower().strip()
        if 'b' in resposta:
            pontos += 10
            print(acerto)
        else:
            print(erro)

        print()
        print('Pergunta 5: Qual é a cor do céu em um dia claro?\na) Azul\nb) Verde\nc) Vermelho')
        resposta = str(input('Resposta: ')).lower().strip()
        if 'a' in resposta:
            pontos += 10
            print(acerto)
        else:
            print(erro)
    if nivel == 2:
        print ()
        print ('Pergunta 1: Quem pintou a Monalisa?\na) Van Gogh \nb) Leonardo da Vinci \nc) Picasso')
        resposta = str(input('Resposta: ')).lower().strip()
        if resposta == 'b':
            pontos += 10
            print(acerto)
        else:
            print(erro)
        print()
        print('Pergunta 2: Qual a fórmula da água?\na) CO2 \nb) H2O \nc) O2')
        resposta = str(input('Resposta: ')).lower().strip()
        if resposta == 'b':
            pontos += 10
            print(acerto)
        else:
            print(erro)
        print()
        print ('Pergunta 3: Qual é o maior oceano do planeta Terra? \na) Atlântico \nb) Índico \nc) Pacífico')
        resposta = str(input('Resposta: ')).lower().strip()
        if resposta == 'c':
            pontos += 10
            print (acerto)
        else:
            print(erro)
        print()
        print('Pergunta 4: Qual o maior país do mundo? \na) Rússia \nb) EUA \nc) China')
        resposta = str(input('Resposta: ')).lower().strip()
        if resposta == 'a':
            pontos += 10
            print (acerto)
        else:
            print(erro)
        print ()
        print('Pergunta 5: Quem desenvolveu a teoria da relatividade? \na) Newton \nb) Einstein \nc) Tesla')
        reposta = str(input('Resposta: ')).lower().strip()
        if reposta == 'b':
            pontos += 10
            print (acerto)
        else:
            print(erro)
    if nivel == 3:
        print ()
        print ('Pergunta 1: Qual o elemento químico mais abundante no universo? \na) Oxigênio \nb) Hidrogênio \nc) Carbono')
        resposta = str(input('Resposta: ')).lower().strip()
        if resposta == 'b':
            pontos += 10
            print (acerto)
        else:
            print(erro)
        print ()
        print ('Pergunta 2: Em que ano ocorreu a queda do muro de Berlim? \na) 1989 \nb) 1991 \nc) 1985')
        resposta = str(input('Resposta: ')).lower().strip()
        if resposta == 'a':
            pontos += 10
            print (acerto)
        else:
            print(erro)
        print ()
        print ('Pergunta 3: Qual o maior osso do corpo humano? \na) Tíbia \nb) Úmero \nc) Fêmur')
        resposta = str(input('Resposta: ')).lower().strip()
        if resposta == 'c':
            pontos += 10
            print (acerto)
        else:
            print(erro)
        print ()
        print ('Pergunta 4: Qual cientista descobriu a gravidade? \na) Galileu \nb) Newton \nc) Kepler')
        resposta = str(input('Resposta: ')).lower().strip()
        if resposta == 'b':
            pontos += 10
            print (acerto)
        else:
            print(erro)
        print ()
        print('Pergunta 5: Qual o nome do processo de divisão celular que forma os gametas? \na) Mitose \nb) Meiose \nc) Fissão')
        resposta = str(input('Resposta: ')).lower().strip()
        if resposta == 'b':
            pontos += 10
            print (acerto)
        else:
            print(erro)
    print()
    print(f'Fim de jogo, {nome}. Sua pontuação final: {pontos} pontos. Parabéns!')
if comando1 == 2:
    print()
    print('Programa Encerrado')