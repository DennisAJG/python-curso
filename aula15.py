""" 
Função input para coleta de dados 
"""

nome = input('Qual é o seu nome: ')
print(f'O seu nome é {nome}')
print(f'O nome do usuário é {nome=}')


numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma entre {numero_1} e {numero_2} é {int_numero_1 + int_numero_2}')