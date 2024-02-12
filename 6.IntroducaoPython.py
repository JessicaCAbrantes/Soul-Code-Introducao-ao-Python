# AULA 01 -----------INTRODUÇÃO STRINGS---------------

nome = "José de Sousa Magalhães"
nome2 = "Rock Perreira Silva"
nome3 = """
Está é uma string longa
contendo inforamações sobre
Python
"""
nome4 ='''
Está é uma string longa
contendo inforamações sobre
Python
'''
print(nome)
print(nome2)
print(nome3)
print(nome4)
"""Execucao: José de Sousa Magalhães
Rock Perreira Silva

Está é uma string longa
contendo inforamações sobre
Python

Está é uma string longa
contendo inforamações sobre
Python
"""



# AULA 02 -----------PROPRIEDADES DAS STRINGS---------------

l = 'lista de letras' #15 os espaços contam
data = '15/09/1991' #len -> tamanho de uma string

#tamanhoda string
tamanho = len(l)
print(tamanho)

#slipt da string (dividir)
lista = l.split(" ")
print(lista)
lista2 = data.split("/")
print(lista2)

#substituição
print(l.replace(" de ", "*"))
"""Execucao: 15
['lista', 'de', 'letras']
['15', '09', '1991']
lista*letras
"""


# AULA 03 -----------FATIANDO UMA STRINGS---------------

#       012345
nome = 'python'
nova_string = nome[5]
print(nova_string)

#       012345
nome = 'python'
nova_string = nome[1:4]
print(nova_string)

#       012345
nome = 'python'
nova_string = nome[1:2:2]
print(nova_string)

#  -6-5-4-3-2-1
nome = 'python'
nova_string = nome[-1]
print(nova_string)
"""Execucao: n
yth
y
n
"""



# AULA 04 -----------COMPARANDO UMA STRINGS---------------

print("a"=="b")
print("b" != "a")
print("a" > "X")
print("a" < "l")
"""Execucao: False
True
False
True
"""




"""for i in range(122):      #caracteres e valores de comparação (retira as aspas e dá para ver valores)
  print(str(i) + " - " +chr(i)) """




# AULA 05 -----------PERCORRENDO STRINGS---------------

nome = 'python'
#for
for i in nome:
  print(i)

print("-------")

#while
i=0
while i <len(nome): # vai rodar apenas a qtidade do nome da string (python)
  print(nome[i])   # imprimir o nome em cada posição
  i+=1              #para não rodar infinito
print("-------")

#for/enumerate
for k, v in enumerate(nome):
  print(k,v)  #k:posição e v:valor -> assumi o papel de
"""Execucao: p
y
t
h
o
n
-------
p
y
t
h
o
n
-------
0 p
1 y
2 t
3 h
4 o
5 n
"""



# AULA 07 -----------ATIVIDADE---------------

alfabeto = 'A B C D F G H I J K L M N O P Q R S T U V X W Y Z'

for k, v in enumerate(alfabeto):
  print(k,v)

print(alfabeto.replace(" ", "-"))
"""Execucao: 0 A
1  
2 B
3  
4 C
5  
6 D
7  
8 F
9  
10 G
11  
12 H
13  
14 I
15  
16 J
17  
18 K
19  
20 L
21  
22 M
23  
24 N
25  
26 O
27  
28 P
29  
30 Q
31  
32 R
33  
34 S
35  
36 T
37  
38 U
39  
40 V
41  
42 X
43  
44 W
45  
46 Y
47  
48 Z
A-B-C-D-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-X-W-Y-Z
"""