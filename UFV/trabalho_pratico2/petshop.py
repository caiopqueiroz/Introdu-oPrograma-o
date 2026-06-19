# Caio Queiroz 7466 
# Pedro Hashimoto 7467
# Bernardo Mansur 7470


# Desenvolver um sistema de controle de atendimentos de um PetShop


# Função para criar um novo atendimento
def novo_atendimento():
    # Criando uma lista para guardar os dados de 1 animal 
    dados = list()
    print('\nNovo atendimento:')
    # Lendo os elementos da lista 
    nome = str(input('Nome do animal: ')).strip().title()
    especie = str(input('Espécie: ')).strip().title()
    print('1 ) Banho e tosa\n2 ) Consulta de rotina\n3 ) Hospedagem')
    servico = int(input('Serviço: '))
    while servico not in [1, 2, 3]:
        print('\033[31;1mServiço inválido\033[m')
        servico = int(input('Serviço: '))
    valor_total = float(input('Valor total: R$'))
    print('1 ) \033[33;1mEm atendimento\033[m\n2 ) \033[34;1mAgendado\033[m\n3 ) \033[32;1mConcluído\033[m\n4 ) \033[31;1mCancelado\033[m')
    status = int(input('Status do atendimento: '))
    while status not in [1, 2, 3, 4]:
        print('\033[31;1mStatus inválido\033[m')
        status = int(input('Status do atendimento: '))
    print('\n\033[32;1mNovo atendimento cadastrado com sucesso!\033[m')
    # Tratando os dados (transformando os números inseridos pelo usuário em palavras)
    for opcao in range(1, 5):
        if opcao == servico:
            if servico == 1:
                servico = 'Banho e tosa'
            elif servico == 2:
                servico = 'Consulta de rotina'
            else:
                servico = 'Hospedagem'
        if opcao == status:
            if status == 1:
                status = '\033[33;1mEm atendimento\033[m'
            elif status == 2:
                status = '\033[34;1mAgendado\033[m'
            elif status == 3:
                status = '\033[32;1mConcluído\033[m'
            else:
                status = '\033[31;1mCancelado\033[m'
    # Colocando as variáveis dentro da lista criada 
    dados.extend([nome, especie, servico, valor_total, status])
    # Retornando a lista como resultado da função
    return dados


# Variáveis 
total_atendimentos = 0
# Criando a matriz em que cada linha é um atendimento
atendimentos = list()


print('\033[34;1m--- Sistema Petshop ---\033[m', end='')
# Criando o looping principal do algoritmo
while True:
    print('\nEscolha uma opção abaixo:\n1 ) Registrar um novo atendimento\n2 ) Buscar pelo nome de um animal\n3 ) Verificar relatório geral do PetShop\n4 ) Sair')
    comando = int(input('Opção: '))
    # Tratamento de erros: fazendo com que o usuário só consiga inserir uma das opções válidas
    while comando not in [1, 2, 3, 4]:
        print('\033[31;1mOpção inválida\033[m')
        comando = int(input('Opção: '))
    if comando == 1:
        # A variável 'ficha' recebendo a lista 'dados' gerada pela função criada anteriormente
        ficha = novo_atendimento()
        # A matriz de atendimentos recebendo a ficha criada
        atendimentos.append(ficha[:])
        total_atendimentos += 1
        comando = 0
    if comando == 2:
        # Criando, apenas para exibição, uma lista de atendimentos que irá conter apenas os animais com o nome buscado pelo usuário
        atendimentos_busca = list()
        busca_nome = str(input('\nNome do animal que deseja buscar: ')).strip().title()
        # Para cada ficha na matriz de atendimentos, caso algum elemento dessa ficha seja o nome do animal buscado, a nova lista 'atendimentos_busca' irá receber a ficha completa desse animal
        for ficha in atendimentos:
            for elemento in ficha:
                if elemento == busca_nome:
                    atendimentos_busca.append(ficha[:])
        # Caso a nova lista criada tenha tamanho 0, isso significa que o animal buscado não existe na matriz de atendimentos original
        if len(atendimentos_busca) == 0:
            print('\n    Esse animal não tem nenhum cadastro')
        else:
            print('\n    Esse animal tem cadastro(s)!')
            numero_atendimento = 1
            # Exibindo as fichas do animal buscado criando um índice numérico para cada uma
            for ficha in atendimentos_busca:
                print(f'\n    \033[34;1m{numero_atendimento}\033[m', end='\033[34;1m ) \033[m')
                for elemento in ficha:
                    print(elemento, end=' | ')
                numero_atendimento += 1
            print('\n\n    Digite o número do atendimento para alterá-lo (0 para não alterar nenhum)')
            # Criando uma forma para alterar o status de um atendimento já cadastrado através do seu índice 
            comando3 = int(input('    Qual atendimento você deseja alterar o status? '))
            if comando3 != 0:
                # Criando uma variável contador
                numero_atendimento = 0
                # Para cada ficha na matriz de atendimentos, caso algum elemento dessa ficha seja o nome do animal buscado, a variável contador recebe +1, dessa forma a contagem bate com o índice criado
                for ficha in atendimentos:
                    for elemento in ficha:
                        if elemento == busca_nome:
                            numero_atendimento += 1
                            # Quando a variável contador bater com o índice selecionado pelo usuário, ele deve inserir um novo status para o atendimento
                            if numero_atendimento == comando3:
                                print('\n    1 ) \033[33;1mEm atendimento\033[m\n    2 ) \033[34;1mAgendado\033[m\n    3 ) \033[32;1mConcluído\033[m\n    4 ) \033[31;1mCancelado\033[m')
                                status = int(input(f'    Novo status do atendimento {numero_atendimento}: '))
                                while status not in [1, 2, 3, 4]:
                                    print('\033[31;1m    Status inválido\033[m')
                                    status = int(input(f'    Novo status do atendimento {numero_atendimento}: '))
                                if status == 1:
                                    status = '\033[33;1mEm atendimento\033[m'
                                elif status == 2:
                                    status = '\033[34;1mAgendado\033[m'
                                elif status == 3:
                                    status = '\033[32;1mConcluído\033[m'
                                else:
                                    status = '\033[31;1mCancelado\033[m'
                                # Fazendo com que o novo status seja atualizado diretamente na matriz original de atendimentos 
                                ficha[4] = status
                                print('\n    \033[32;1mAtendimento atualizado com sucesso!\033[m')
            else:
                pass
        comando = 0
    if comando == 3:
        # Definindo as variáveis com o valor 0 para serem atualizadas a cada execução
        total_arrecadado = 0
        cancelados = 0
        # Para cada ficha na matriz de atendimentos, se o status for 'Concluído', o dinheiro ganho será somado, e se for 'Cancelado', o número de atendimentos cancelados aumentará
        for ficha in atendimentos:
            if ficha[4] == '\033[32;1mConcluído\033[m':
                total_arrecadado += ficha[3]
            if ficha[4] == '\033[31;1mCancelado\033[m':
                cancelados += 1
        print('\n\033[34;1m--- Relatório Geral Petshop ---\033[m')
        print(f'Total de atendimentos registrados: {total_atendimentos}')
        print(f'Total de atendimentos cancelados: {cancelados}')
        print(f'Total arrecadado com atendimentos concluídos: R${total_arrecadado:.2f}')
        comando = 0
    # Finalizando o looping
    if comando == 4:
        break
   

    