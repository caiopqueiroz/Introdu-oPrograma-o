print("Bem vindo ao GeoQuiz")
print()
print("1 - Jogar")
print("2 - Sair")
print()

opcao = input("Escolha: ")

if opcao == "1":
    nome = input("Digite seu nome: ")
    print("\nEscolha o nível:")
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")

    nivel = input("Nível: ")
    pontos = 0

    if nivel == "1":
        print("\nNível fácil")

        print("\n1. Qual é a capital da Argentina?")
        print("a) Buenos Aires")
        print("b) Santiago")
        print("c) Montevidéu")
        r = input("Resposta: ")
        if r == "a":
            print("Acertou")
            pontos = pontos + 10
        else:
            print("Errou")

        print("\n2. Qual é a capital do Chile?")
        print("a) Lima")
        print("b) Santiago")
        print("c) Bogotá")
        r = input("Resposta: ")
        if r == "b":
            print("Acertou")
            pontos = pontos + 10
        else:
            print("Errou")

        print("\n3. Qual é a capital do Uruguai?")
        print("a) Quito")
        print("b) Montevidéu")
        print("c) Assunção")
        r = input("Resposta: ")
        if r == "b":
            print("Acertou")
            pontos = pontos + 10
        else:
            print("Errou")

        print("\n4. Qual é a capital do Peru?")
        print("a) Lima")
        print("b) Caracas")
        print("c) La Paz")
        r = input("Resposta: ")
        if r == "a":
            print("Acertou")
            pontos = pontos + 10
        else:
            print("Errou")

        print("\n5. Qual é a capital da Colômbia?")
        print("a) Bogotá")
        print("b) Brasília")
        print("c) Paramaribo")
        r = input("Resposta: ")
        if r == "a":
            print("Acertou")
            pontos = pontos + 10
        else:
            print("Errou")

        print("\nFim do jogo,", nome)
        print("Sua pontuação foi:", pontos)

    elif nivel == "2":
        print("\nNível médio")

        print("\n1. Qual é a capital de Minas Gerais?")
        print("a) Belo Horizonte")
        print("b) Goiânia")
        print("c) Curitiba")
        r = input("Resposta: ")
        if r == "a":
            print("Acertou")
            pontos = pontos + 10
        else:
            print("Errou")

        print("\n2. Qual é a capital da Bahia?")
        print("a) Recife")
        print("b) Fortaleza")
        print("c) Salvador")
        r = input("Resposta: ")
        if r == "c":
            print("Acertou")
            pontos = pontos + 10
        else:
            print("Errou")

        print("\n3. Qual é a capital do Paraná?")
        print("a) Florianópolis")
        print("b) Porto Alegre")
        print("c) Curitiba")
        r = input("Resposta: ")
        if r == "c":
            print("Acertou")
            pontos = pontos + 10
        else:
            print("Errou")

        print("\n4. Qual é a capital de Pernambuco?")
        print("a) Recife")
        print("b) Natal")
        print("c) João Pessoa")
        r = input("Resposta: ")
        if r == "a":
            print("Acertou")
            pontos = pontos + 10
        else:
            print("Errou")

        print("\n5. Qual é a capital do Pará?")
        print("a) Manaus")
        print("b) Belém")
        print("c) Macapá")
        r = input("Resposta: ")
        if r == "b":
            print("Acertou")
            pontos = pontos + 10
        else:
            print("Errou")

        print("\nFim do jogo,", nome)
        print("Sua pontuação foi:", pontos)

    elif nivel == "3":
        print("\nNível difícil")

        print("\n1. Qual é a capital da Turquia?")
        print("a) Istambul")
        print("b) Ancara")
        print("c) Esmirna")
        r = input("Resposta: ")
        if r == "b":
            print("Acertou")
            pontos = pontos + 10
        else:
            print("Errou")

        print("\n2. Tóquio é a capital de qual país?")
        print("a) Japão")
        print("b) China")
        print("c) Coreia do Sul")
        r = input("Resposta: ")
        if r == "a":
            print("Acertou")
            pontos = pontos + 10
        else:
            print("Errou")

        print("\n3. O Egito fica em qual continente?")
        print("a) Europa")
        print("b) Ásia")
        print("c) África")
        r = input("Resposta: ")
        if r == "c":
            print("Acertou")
            pontos = pontos + 10
        else:
            print("Errou")

        print("\n4. Cairo é a capital de qual país?")
        print("a) Egito")
        print("b) Marrocos")
        print("c) Arábia Saudita")
        r = input("Resposta: ")
        if r == "a":
            print("Acertou")
            pontos = pontos + 10
        else:
            print("Errou")

        print("\n5. A Índia fica em qual continente?")
        print("a) Oceania")
        print("b) Ásia")
        print("c) Europa")
        r = input("Resposta: ")
        if r == "b":
            print("Acertou")
            pontos = pontos + 10
        else:
            print("Errou")

        print("\nFim do jogo,", nome)
        print("Sua pontuação foi:", pontos)

    else:
        print("Nível inválido")

elif opcao == "2":
    print("Saindo...")

else:
    print("Opção inválida")