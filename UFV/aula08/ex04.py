# verificar quantos dias faltam para consulta médica 
# programa deverá permitir vários agendamentos


from datetime import datetime

for vez in range(0, 5):
    nome_paciente = str(input('\nNome do paciente: ')).strip().title()
    data_consulta = str(input('Data da consulta (DD/MM/AAAA): ')).strip()
    data = data_consulta.split('/')
    dia_consulta = int(data[0])
    mes_consulta = int(data[1])
    ano_consulta = int(data[2])
    dia_atual = datetime.now().day
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year
    data_consulta = datetime(ano_consulta, mes_consulta, dia_consulta)
    data_atual = datetime(ano_atual, mes_atual, dia_atual)
    dias_faltantes = data_consulta - data_atual
    print(f'\nNome do paciente: {nome_paciente}')
    print(f'Data atual: {dia_atual}/{mes_atual}/{ano_atual}')
    print(f'Data da consulta: {dia_consulta}/{mes_consulta}/{ano_consulta}')
    print(f'Faltam {dias_faltantes.days} dias para a consulta')