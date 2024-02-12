# AULA 01 -----------INTRODUÇÃO A TUPLAS---------------

t = tuple("abc")
x = ("pyhton","curso")
x1 = (2,3,4)
x2 = (2.1, 2.3, 2.5)
x3 = ("pyhton", 1, 1.5, True)
print(x3)
print(type(x2))
"""Execucao: ('pyhton', 1, 1.5, True)
<class 'tuple'>
"""



# AULA 02 -----------OPERAÇÕES COM TUPLAS---------------

elementos_tupla = ('São Paulo', 'Belo Horizonte', 'Teresina')
print('Manaus' in elementos_tupla)
print('São Paulo' in elementos_tupla)

#                 0        1         2       3        4        5
nomes_tupla = ('José', 'Carlos', 'Maria', 'Pedro', 'Joana', 'Maria')
print(nomes_tupla.count('Maria'))
print(nomes_tupla.index('Carlos'))
"""Execucao: False
True
2
1
"""