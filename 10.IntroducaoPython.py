# AULA 01 -----------INTRODUÇÃO A FUNÇÔES---------------

def funcao():
  print("Eu sou uma função!")

funcao()  #chamando
""" Execucao: Eu sou uma função!"""



# AULA 02 -----------PARÂMETROS DE FUNÇÔES---------------

def soma(x, y):
  total = x + y
  print(total)

soma(2,4)
"""Execucao:6"""



# AULA 04 -----------RETORNO DE FUNÇÔES---------------

def show():
  return 15

print(show())
15

def mult(a, b):
  return a * b

print (mult(2,5))
"""Execucao:10"""



# AULA 05 -----------ATIVIDADE---------------

def funcao(a, b):
  total = a + b
  total1 = a - b
  total2 = a * b
  total3 = a / b

  print(total)
  print(total1)
  print(total2)
  print(total3)

funcao(5, 7)
"""Execucao: 12
-2
35
0.7142857142857143"""




# AULA 06 -----------CORREÇÃO---------------

def operacoes (a, b):
  soma = a + b
  sub = a - b
  mult = a * b
  div = a /b

  print("Soma: ", soma)
  print("Subtração: ", sub)
  print("Subtração: ", mult)
  print("Divisão: ", div)

operacoes(4, 2)
"""Execucao: Soma:  6
Subtração:  2
Subtração:  8
Divisão:  2.0"""



#ATIVIDADE FINAL

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

def multiplicar(a, b):
    return a * b

def listar():
    vantagens = [
        "Sintaxe simples e legível",
        "Ampla biblioteca padrão",
        "Portabilidade entre plataformas",
        "Suporte a programação orientada a objetos",
        "Grande comunidade de desenvolvedores",
    ]

    for vantagem in vantagens:
        print(vantagem)

print("Bem-vindo ao Menu de Operações!")
print("1. Somar")
print("2. Subtrair")
print("3. Dividir")
print("4. Multiplicar")
print("5. Listar vantagens do Python")

escolha = input("Escolha uma opção (1-5): ")

if escolha == "1":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = somar(num1, num2)
    print("Resultado: ", resultado)

elif escolha == "2":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = subtrair(num1, num2)
    print("Resultado: ", resultado)

elif escolha == "3":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = dividir(num1, num2)
    print("Resultado: ", resultado)

elif escolha == "4":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = multiplicar(num1, num2)
    print("Resultado: ", resultado)

elif escolha == "5":
    print("Vantagens do Python:")
    listar()

else:
    print("Opção inválida.")
"""Execucao: Bem-vindo ao Menu de Operações!
1. Somar
2. Subtrair
3. Dividir
4. Multiplicar
5. Listar vantagens do Python
Escolha uma opção (1-5): 2
Digite o primeiro número: 6
Digite o segundo número: 7
Resultado:  -1.0
"""