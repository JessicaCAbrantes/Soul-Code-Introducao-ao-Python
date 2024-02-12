# AULA 01 -----------ESTRUTURAS DE CONTROLE DE FLUXO---------------

#Laço While

i = 1

while(i<=10):
  print("O loop está rodando...")
  print (i)
  i+=1  #i é igual i+1...=2 +1...

"""Execucao: O loop está rodando...
1
O loop está rodando...
2
O loop está rodando...
3
O loop está rodando...
4
O loop está rodando...
5
O loop está rodando...
6
O loop está rodando...
7
O loop está rodando...
8
O loop está rodando...
9
O loop está rodando...
10
"""


# AULA 02 -----------LAÇO DE REPETIÇÃO FOR---------------

for i in "Python":
  print(i)
"""Execucao: P
y
t
h
o
n
"""

num = [1,5,6,7]

for j in num:
  print(j)
"""Execucao: 1
5
6
7
"""



# AULA 03 -----------LAÇO FOR RANGE---------------

for i in range(10):
  print(i)

"""Execucao: 0
1
2
3
4
5
6
7
8
9
"""

for i in range(10):
  print("Olá mundo")
"""Execucao: Olá mundo
Olá mundo
Olá mundo
Olá mundo
Olá mundo
Olá mundo
Olá mundo
Olá mundo
Olá mundo
Olá mundo
"""

for i in range(10):
  print(i+1)
"""Execucao: 1
2
3
4
5
6
7
8
9
10
"""

for i in range(9, -1, -1):
  print(i)
"""Execucao: 9
8
7
6
5
4
3
2
1
0
"""



# AULA 04 -----------ATIVIDADE---------------

for i in range(0,15):      #ERREI
  print(i*3)
"""Execucao: 0
3
6
9
12
15
18
21
24
27
30
33
36
39
42
"""



# AULA 05 -----------CORREÇÃO---------------

for i in range(0, 15, 3):
  print(i)
"""Execucao: 0
3
6
9
12
"""



# AULA 06 -----------INSTRUÇÃO BREAK E CONTINUE---------------

# Break

for i in range(10):
  print(i)
  if (i == 5):
      break
"""Execucao: 0
1
2
3
4
5
"""

i = 0
while (i<10):
  i+=1
  if (1%2==0): #é par
    continue
  print(i)
"""Execucao: 1
2
3
4
5
6
7
8
9
10
"""