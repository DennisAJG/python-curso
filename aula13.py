""" 
f-strings
"""

nome = 'Dennis'
altura = 1.83
peso = 90
imc = peso / altura ** 2
test = ... # Ellipsis
linha =f'{nome} tem {altura} de altura e {peso} de peso e seu IMC e {imc:.2f}'
print(linha)
print(f'{nome} tem {altura} de altura e {peso} de peso e seu IMC e {imc:.2f}')