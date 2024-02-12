# AULA 01 ----------- OPERADORES DE CONDIÇÕES E RELAÇÃO---------------

#Operadores de Igualdade
# ==, !=

a = 2 # o valor 2 está sendo atribuido a variável a
a == 2 # quer verificar se a é igual a 2
a != 2 # quer verificar se a é diferente de 2

#Operadores de Relacionais
# >, <, >=, <=

"""
x > y
x <= y

Execucao:True"""



# AULA 03 ----------- COMANDO IF E ELSE---------------

numero = 11

if numero == 10:
  print ("Este número é igual a 10!")
else: #False
  print("Este número não é igual a 10!")

numero2 = 10

if numero2 == 10:
  print ("Este número é igual a 10!")
else: #False
  print("Este número não é igual a 10!")

"""Execucao:Este número não é igual a 10!
Este número é igual a 10!"""



# AULA 04 ----------- COMANDO ELIF ---------------

numero = 12

if numero == 10:
  print ("Este número é igual a 10!")
elif numero == 11:
  print("Este número não é igual a 11!")
elif numero == 12:
  print("Este número não é igual a 12!")
elif numero == 13:
  print("Este número não é igual a 13!")
else:
  print("Esse número não é igual nem a 10, 11, 12 ou 13!")
"""Execucao: Este número não é igual a 12!"""



# AULA 05 ----------- ATIVIDADE---------------

numero = 15

if numero == 15:
  print("Este número é igual a 15!")
elif numero < 15:
  print("Este número menor que 15!")
else:
  print("Este número maior que 15!")
"""Execucao: Este número igual que 15!"""



# AULA 06 ----------- CORREÇÃO---------------

numero = 16

if numero == 15:
  print("Este número é igual a 15!")
elif numero < 15:
  print("Este número menor que 15!")
elif numero > 15:
  print("Este número maior que 15!")
"""Execucao: Este número maior que 15!"""