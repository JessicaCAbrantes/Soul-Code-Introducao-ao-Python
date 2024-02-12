# AULA 01 ----------- SAÍDA DE DADOS---------------

print("Olá mundo!")
"""Execucao: Olá mundo!"""

nome = "José"
idade = 30
peso = 70.4

print(nome)
print(idade)
print(peso)

"""Execucao: José
30
70.4
"""

nome = "José"

print("Meu nome é", nome, "e minha idade é", idade, ".")
"""Execucao: Meu nome é José e minha idade é 30 ."""

print('02', '11', '2023', sep='/')
"""Execucao: 02/11/2023"""

print('2023', '11', '23', sep="-")
"""Execucao: 2023-11-23"""

print("B", "n", "n", '.', sep='a')
"""Execucao: Banana."""



# AULA 02 ----------- ENTRADA DE DADOS---------------


nome = input("Escreva seu nome:")
"""Execucao: Escreva seu nome:José"""

nome = input("Escreva seu nome: ") #string
idade = int(input("Excreva sua idade: ")) #inteiro
peso = float(input("Escreva seu peso: ")) #float
"""Execucao: Escreva seu nome: Jose
Excreva sua idade: 45
Escreva seu peso: 74 """



# AULA 03 ----------- OPERADORES ARITMÉTICOS---------------

# +, -, /, *, //, %

a = 4
b = 4

print(a + b) #adição
print(5 - 2) #subtração
print(3 * 2) #multiplicação
print(10 /6) #divisão
print(10 // 6) #divisão exata
print(10 % 3) # resto
"""Execucao: 8
3
6
1.6666666666666667
1
1"""



# AULA 04 ----------- ATIVIDADE---------------

nome = input("Escreva o seu nome: ")
altura = float(input("Excreva sua altura: "))
CPF = int(input("Escreva o seu CPF: "))

print("Seus dados são: ", nome, altura, CPF, sep="-")
"""Execucao: Escreva o seu nome: Jessi
Excreva sua altura: 160
Escreva o seu CPF: 22222222274
Seus dados são: -Jessi-160.0-22222222274
"""



# AULA 05 ----------- CORREÇÃO---------------

nome = input("Digite o seu nome: ")
altura = float(input("Digite sua altura: "))
cpf = int(input("Digite seu CPF: "))

print("O nome digitado é: ", nome,". A altura digitada é: ", altura,". O CPF digitado é: ", cpf,"." )
"""Execucao: Digite o seu nome: Jessica
Digite sua altura: 160
Digite seu CPF: 22222222274
O nome digitado é:  Jessica . A altura digitada é:  160.0 . O CPF digitado é:  22222222274 ."""