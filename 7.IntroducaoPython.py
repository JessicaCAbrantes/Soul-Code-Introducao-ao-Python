# AULA 01 -----------INTRODUÇÃO A LISTAS---------------

nome = 'python'
lista = [1,2,3,4,5]
lista2 = [1.2,2.3,6.5]
lista3 = [2,1.5,"número"]
lista4 =  []

print(lista2[1])
"""Execucao: 2.3 """



# AULA 02 -----------PERCORRENDO LISTAS---------------

lista = [100,200,300,400,500,600,700,800]

for i in range(len(lista)):
  print(lista[i])

print(lista)
"""Execucao: 100
200
300
400
500
600
700
800
[100, 200, 300, 400, 500, 600, 700, 800]
"""



# AULA 03 -----------FATIANDO LISTAS---------------

#        0 1 2
lista = [2,3,4]
#       -3-2-1

nova_lista = lista[0:2:2]
print(nova_lista)

lista2 = ['p', 'y', 't', 'h', 'o', 'n']
nova_lista2 = lista2[::-1]  #-1 começa pelo ultimo elemento :: tudo pq não tem os elementos
print(nova_lista2)
"""Execucao: [2]
['n', 'o', 'h', 't', 'y', 'p']
"""



# AULA 04 -----------ATIVIDADE---------------

lista = ['P', 'Y', 'T', 'H', 'O', 'N']

nova_lista = lista[3:6]
print(nova_lista)
"""Execucao:['H', 'O', 'N'] """




# AULA 05 -----------CORREÇÃO---------------

lista = ['P', 'Y', 'T', 'H', 'O', 'N']
nova_lista = lista[3:6]
print(nova_lista)
"""Execucao:  ['H', 'O', 'N']"""

# AULA 06 -----------Incluir, alterar, excluir elemento de listas---------------

animais = ['Gato', 'Cachorro','Elefante']
print(animais)

animais.append('Galinha')  #inclui por último
print(animais)

animais.insert(0,"Papagaio")   #inclui aonde você quiser
print(animais)

animais.pop(0)    #exclui aonde você quiser número
print(animais)

animais.remove('Gato')    #exclui pelo nome
print(animais)
"""Execucao: ['Gato', 'Cachorro', 'Elefante']
['Gato', 'Cachorro', 'Elefante', 'Galinha']
['Papagaio', 'Gato', 'Cachorro', 'Elefante', 'Galinha']
['Gato', 'Cachorro', 'Elefante', 'Galinha']
['Cachorro', 'Elefante', 'Galinha']
"""



# AULA 07 -----------ORDENAR LISTAS---------------

lista = ['a', 'x', 's', 'w', 'd', 'a', 'n', 'a']
#lista.reverse()
lista.sort()

print(lista)

for i in range(len(lista)):
  print(lista[i])

l = lista.count('a')
print(l)
"""Execucao:['a', 'a', 'a', 'd', 'n', 's', 'w', 'x']
a
a
a
d
n
s
w
x
3
"""



# AULA 08 -----------ATIVIDADE---------------

moveis_casa = ['sofá', 'tv', 'cama', 'guarda-roupa', 'mesa', 'computador']

moveis_casa.append('cadeira')
print(moveis_casa)

moveis_casa.remove("guarda-roupa")
print(moveis_casa)
"""Execucao: ['sofá', 'tv', 'cama', 'guarda-roupa', 'mesa', 'computador', 'cadeira']
['sofá', 'tv', 'cama', 'mesa', 'computador', 'cadeira']
"""



# AULA 09 -----------CORREÇÃO-----------

lista = ['Cadeira', 'Mesa', 'Sofá']
lista.append('Cama')
lista.pop(0)
print(lista)
"""Execucao: ['Mesa', 'Sofá', 'Cama']
"""