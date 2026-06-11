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
    print('\nNovo atendimento:\n')
    nome = str(input('Nome do animal: ')).strip().title()
    especie = str(input('Espécie: ')).strip().title()
    print('1 ) Banho e tosa\n2 ) Consulta de rotina\n3 ) Hospedagem')
    servico = int(input('Serviço: '))
    valor_total = float(input('Valor total: R$'))
    status = str(input('Status do atendimento: ')).strip()
    dados.extend([nome, especie, servico, valor_total, status])
    return dados


# variáveis
comando = 0
#atendimentos = list()
atendimentos = [['Lubil']]

print('Bem-vindo(a)')
while True:
    print('\n1 ) Registrar um novo atendimento\n2 ) Buscar pelo nome de um animal\n3 ) Verificar relatório geral do PetShop')
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
        print('    2.1 ) Verificar todos os seus atendimentos\n    2.2 ) Atualizar status de um atendimento')
        comando2 = int(input('    Opção: '))
        if len(atendimentos_busca) == 0:
            print('Esse animal não tem nenhum cadastro')
        else:
            print('Esse animal tem cadastro(s)!')
            if comando2 == 1:
                for ficha in atendimentos_busca:
                    print(ficha)
            if comando2 == 2:
                contador = 1
                for ficha in atendimentos_busca:
                    print(contador, end=' ) ')
                    print(ficha)
                    contador += 1
                comando3 = int(input('Qual atendimento você deseja alterar o status? '))
        comando = 0
    if comando == 9:
        break
    
#   

    