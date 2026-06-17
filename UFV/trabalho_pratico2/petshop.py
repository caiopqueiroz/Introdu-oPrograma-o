# Desenvolver um sistema de controle de atendimentos de um PetShop

# usuário (que é funcionário do petshop) vai preencher um cadastro:
# nome do animal 
# espécie
# serviço contratado
# valor total
# status (agendado, em atendimento, concluído, cancelado) 

# o que o programa deve fazer?
# registrar um atendimento
# verificar se o animal já está cadastrado e mudar o seu status
# quando o status se tornar concluído, o atendimento estará finalizado
# permitir uma busca pelo nome do animal e listar todos os atendimentos dele
# deve ser possível checar um relatório geral, que mostra:
# total de atendimentos
# valor total arrecadado com atendimentos concluídos
# quantidade de atendimentos cancelados
 
# opções:
# 1 ) Registrar um novo atendimento
# 2 ) Buscar pelo nome de um animal
    # 2.1 ) Verificar todos os seus atendimentos
    # 2.2 ) Atualizar status de um atendimento
# 3 ) Verificar relatório geral do petshop


def novo_atendimento():
    dados = list()
    print('\nNovo atendimento:')
    nome = str(input('Nome do animal: ')).strip().title()
    especie = str(input('Espécie: ')).strip().title()
    print('1 ) Banho e tosa\n2 ) Consulta de rotina\n3 ) Hospedagem')
    servico = int(input('Serviço: '))
    while servico not in [1, 2, 3]:
        print('\033[31;1mServiço inválido\033[m')
        servico = int(input('Serviço: '))
    valor_total = float(input('Valor total: R$'))
    print('1 ) Em atendimento\n2 ) Agendado\n3 ) Concluído\n4 ) Cancelado')
    status = int(input('Status do atendimento: '))
    while status not in [1, 2, 3, 4]:
        print('\033[31;1mStatus inválido\033[m')
        status = int(input('Status do atendimento: '))
    print('\n\033[32;1mNovo atendimento cadastrado com sucesso\033[m')
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
                status = 'Em atendimento'
            elif status == 2:
                status = 'Agendado'
            elif status == 3:
                status = 'Concluído'
            else:
                status = 'Cancelado'
    dados.extend([nome, especie, servico, valor_total, status])
    return dados


# variáveis
comando = 0
total_atendimentos = 0
atendimentos = list()
#atendimentos = [['Lubil', 'Gato', 1, 10, 'em atendimento']]

while True:
    print('\nEscolha uma opção abaixo:\n1 ) Registrar um novo atendimento\n2 ) Buscar pelo nome de um animal\n3 ) Verificar relatório geral do PetShop')
    while comando not in [1, 2, 3, 9]:
        comando = int(input('Opção: '))
    if comando == 1:
        ficha = novo_atendimento()
        atendimentos.append(ficha[:])
        total_atendimentos += 1
        comando = 0
    if comando == 2:
        atendimentos_busca = list()
        busca_nome = str(input('\nNome do animal que deseja buscar: ')).strip().title()
        for ficha in atendimentos:
            for elemento in ficha:
                if elemento == busca_nome:
                    atendimentos_busca.append(ficha[:])
        if len(atendimentos_busca) == 0:
            print('\n    Esse animal não tem nenhum cadastro')
        else:
            print('\n    Esse animal tem cadastro(s)!')
            numero_atendimento = 1
            for ficha in atendimentos_busca:
                print(f'\n    {numero_atendimento}', end=' ) ')
                for elemento in ficha:
                    print(elemento, end=' | ')
                numero_atendimento += 1
            print('\n\n    Digite o número do atendimento para alterá-lo (0 para não alterar nenhum)')
            comando3 = int(input('    Qual atendimento você deseja alterar o status? '))
            if comando3 != 0:
                numero_atendimento = 0
                for ficha in atendimentos:
                    for elemento in ficha:
                        if elemento == busca_nome:
                            numero_atendimento += 1
                            if numero_atendimento == comando3:
                                print('\n    1 ) Em atendimento\n    2 ) Agendado\n    3 ) Concluído\n    4 ) Cancelado')
                                status = int(input(f'    Novo status do atendimento {numero_atendimento}: '))
                                while status not in [1, 2, 3, 4]:
                                    print('\033[31;1m    Status inválido\033[m')
                                    status = int(input(f'    Novo status do atendimento {numero_atendimento}: '))
                                if status == 1:
                                    status = 'Em atendimento'
                                elif status == 2:
                                    status = 'Agendado'
                                elif status == 3:
                                    status = 'Concluído'
                                else:
                                    status = 'Cancelado'
                                ficha[4] = status
                print('\n    \033[32;1mAtendimento atualizado com sucesso!\033[m')
            else:
                pass
        comando = 0
    if comando == 3:
        total_arrecadado = 0
        cancelados = 0
        for ficha in atendimentos:
            if ficha[4] == 'Concluído':
                total_arrecadado += ficha[3]
            if ficha[4] == 'Cancelado':
                cancelados += 1
        print('\n\033[34;1m--- Relatório Geral Petshop ---\033[m')
        print(f'Total de atendimentos registrados: {total_atendimentos}')
        print(f'Total de atendimentos cancelados: {cancelados}')
        print(f'Total arrecadado com atendimentos concluidos: R${total_arrecadado:.2f}')
        comando = 0
    if comando == 9:
        break
    
#   

    