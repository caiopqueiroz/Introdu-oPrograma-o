from random import choice


opcoes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Ás', 'Valete', 'Dama', 'Rei']
naipes = ['Espadas', 'Ouros', 'Paus', 'Copas']
print(f'A carta sorteada foi: {choice(opcoes)} de {choice(naipes)}')