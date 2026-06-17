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
    valor_total = float(input('Valor total: R$'))
    status = str(input('Status do atendimento: ')).strip()
    print('\n\033[32mNovo atendimento cadastrado com sucesso\033[m')
    dados.extend([nome, especie, servico, valor_total, status])
    return dados


# variáveis
comando = 0
#atendimentos = list()
atendimentos = [['Lubil', 'Gato', 1, 10, 'em atendimento']]

while True:
    print('\nEscolha uma opção abaixo:\n1 ) Registrar um novo atendimento\n2 ) Buscar pelo nome de um animal\n3 ) Verificar relatório geral do PetShop')
    while comando not in [1, 2, 3, 9]:
        comando = int(input('Opção: '))
    if comando == 1:
        ficha = novo_atendimento()
        atendimentos.append(ficha[:])
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
            print('\n\n    Digite o número do atendimento para alterá-lo\n    Digite 0 para não alterar nenhum')
            comando3 = int(input('    Qual atendimento você deseja alterar o status? '))
            if comando3 != 0:
                numero_atendimento = 0
                for ficha in atendimentos:
                    for elemento in ficha:
                        if elemento == busca_nome:
                            numero_atendimento += 1
                            if numero_atendimento == comando3:
                                ficha[4] = str(input(f'\n    Novo status do atendimento {numero_atendimento}: '))
                print('\n    \033[32mAtendimento atualizado com sucesso!\033[m')
            else:
                pass
        comando = 0
    if comando == 3:
        pass
        comando = 0
    if comando == 9:
        break
    
#   

    