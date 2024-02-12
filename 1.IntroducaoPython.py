#UNIDADE II
# AULA 04 ----------- COMENTÁRIOS---------------

# Está linha imprime um texto (comentário de 1 linha).
print ("Olá mundo!")

"""Execucao: Olá mundo!"""

'''
Este é um comentário
longo do
Python
'''

"""
Este é um comentário
longo do
Python
"""



# AULA 05 ----------- INDENTAÇÃO---------------

x = 0
y = 0
if x ==0:
  print("x é igual a 10.")
  print("x é igual a 10.")
  if y == 0:
    print("x é igual a 10.")

print("x é igual a 10.")

"""Execucao: x é igual a 10.
x é igual a 10.
x é igual a 10.
x é igual a 10.
"""



# AULA 06 ----------- VARIÁVEIS---------------

''' Em algumas linguagens você terá que declarar o tipo de variável, no Python
não é necessário, poque ele é dinâmico.
'''
idade = 32  #variável número inteiro - n° não fracionado (int)
peso = 65.4 #variável número ?double ou float (ponto não vírgula)
nome = "José" #variavél tipo string (armazena um texto - cadeias de caracteres)

peso2 = "65.4" # dentro de "_"será considerado texto e não poderá fazer cálculos com ele

situacao = True  #variável boolean retorna = V ou F
situacao2 = False #variável boolean



# AULA 07 ----------- TIPOS DE VARIÁVEIS ---------------

idade = 32
peso = 65.4
nome = "José"
peso2 = "65.4"
situacao = True
situacao2 = False

type(idade)
type(peso)
#string
type(nome)
#booleana
type(situacao)

"""Execucao: bool"""



# AULA 08 ----------- ATIVIDADE ---------------

# Comentário longo: Este é um script simples em Python que demonstra o uso de variáveis para representar informações sobre animais.

# Variáveis representando informações sobre os animais
animal1 = "Cachorro"  # Comentário curto: nome do primeiro animal
animal2 = "Gato"      # Comentário curto: nome do segundo animal
animal3 = "Pássaro"   # Comentário curto: nome do terceiro animal
animal4 = "Cobra"     # Comentário curto: nome do quarto animal
quantidade_animais = 10  # Comentário curto: quantidade total de animais
peso_animais = [10.5, 7.2, 0.3, 23, 9, 1, 7, 0.5, 12, 4]  # Comentário curto: lista de pesos dos animais em ordem
vacinados = [True, False, True, True, False, True, False, True, False, False]  # Comentário curto: lista de booleanos indicando se os animais estão vacinados

# Impressão das informações
print("Informações sobre os animais:")
print("Nome do animal:", animal1, animal2, animal3, animal4)
print("Quantidade de animais:", quantidade_animais)
print("Pesos dos animais:", peso_animais)
print("Animais vacinados:", vacinados)

"""Execucao: Informações sobre os animais:
Nome do animal: Cachorro Gato Pássaro Cobra
Quantidade de animais: 10
Pesos dos animais: [10.5, 7.2, 0.3, 23, 9, 1, 7, 0.5, 12, 4]
Animais vacinados: [True, False, True, True, False, True, False, True, False, False]
"""



# AULA 09 ----------- CORREÇÃO---------------
'''
Aqui temos as variáveis com
nomes, quantidades e peso
dos animais e...
'''
animal1 = "Leão"
animal2 = "Tartaruga"
animal3 = "Cachorro"

quantidade_de_animais = 3

peso_animal1 = 60.8
peso_animal2 = 32.7
peso_animal3 = 25.4

#Situação da vacinação

situacao_animal1 = False
situacao_animal2 = False
situacao_animal3 = True

