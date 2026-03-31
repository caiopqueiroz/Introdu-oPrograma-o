# Faça um programa que solicite ao usuário a idade, o sexo e o tempo de serviço de
# um trabalhador e escreva se ele pode ou não se aposentar. As condições para
# aposentadoria para quem é do sexo masculino são:
# • Ter pelo menos 65 anos,
# • E ter trabalhado pelo menos 30 anos.
# Se for do sexo feminino:
# • Ter pelo menos 60 anos,
# • E ter trabalhado pelo menos 25 anos


idade = int(input('Idade: '))
sexo = str(input('Sexo (M ou F): ')).strip().upper()
tempo = int(input('Anos de serviço: '))
if sexo[0] == 'M' and idade >= 65 and tempo >= 30:
    print('Parabéns! O senhor já pode se aposentar.')
elif sexo[0] == 'F' and idade >= 60 and tempo >= 25:
    print('Parabéns! A senhora já pode se aposentar.')
else:
    print('Infelizmente sua aposentadoria ainda não será possível.')

