# AULA 01 -----------INTRODUÇÃO AO DICIONÁRIOS---------------

dicionario = {"a": "amor", "b":"blue"}
dicionario2 = {1:20,3:30,4:30}
dicionario3 = {5.5:50.50, 30.1:30.25}
dicionario4 = {(10,20):["python","linguagem",10]}
print (dicionario)
print(type(dicionario))

"""Execucao: {'a': 'amor', 'b': 'blue'}
<class 'dict'>
"""



# AULA 02 -----------ACESSANDO AOS DICIONÁRIOS---------------

dicionario = {"a":"letraA", "b":"letraB", "c":"letraC"}
print(dicionario["a"])
print(dicionario.get('d', 'Valor não encontrado!'))
"""Execucao: letraA
Valor não encontrado!
"""



# AULA 03 -----------FUNÇÕES COM DICIONÁRIOS---------------

agenda = {40408021:"José", 87541236:"Heloise", 78945612:"Carloa", 36925874:"Claudio" }
print(agenda)
del(agenda[40408021])
print(agenda)
print("---------------------------")
print(agenda.keys())
print(agenda.values())
print("---------------------------")
print(agenda.popitem())
print(agenda.popitem())
print(agenda)

"""Execucao
{40408021: 'José', 87541236: 'Heloise', 78945612: 'Carloa', 36925874: 'Claudio'}
{87541236: 'Heloise', 78945612: 'Carloa', 36925874: 'Claudio'}
---------------------------
dict_keys([87541236, 78945612, 36925874])
dict_values(['Heloise', 'Carloa', 'Claudio'])
---------------------------
(36925874, 'Claudio')
(78945612, 'Carloa')
{87541236: 'Heloise'}
"""



#AULA 04 -----------ATIVIDADE---------------

dicionario = {"dia1":"domingo", "dia2":"segunda-feira","dia3":"terça-feira","dia4":"quarta-feira","dia5":"quinta-feira","dia6":"sexta-feira","dia7":"sábado"}
print(dicionario)
del(dicionario["dia7"])
print(dicionario)
del(dicionario["dia6"])
print(dicionario)
print("---------------------------")
del(dicionario["dia2"])
print(dicionario)
print("---------------------------")
dicionario = {"dia1":"domingo", "dia2":"segunda-feira","dia3":"terça-feira","dia4":"quarta-feira","dia5":"quinta-feira","dia6":"sexta-feira","dia7":"sábado"}
print(dicionario)
print("---------------------------")

"""Execucao
{'dia1': 'domingo', 'dia2': 'segunda-feira', 'dia3': 'terça-feira', 'dia4': 'quarta-feira', 'dia5': 'quinta-feira', 'dia6': 'sexta-feira', 'dia7': 'sábado'}
{'dia1': 'domingo', 'dia2': 'segunda-feira', 'dia3': 'terça-feira', 'dia4': 'quarta-feira', 'dia5': 'quinta-feira', 'dia6': 'sexta-feira'}
{'dia1': 'domingo', 'dia2': 'segunda-feira', 'dia3': 'terça-feira', 'dia4': 'quarta-feira', 'dia5': 'quinta-feira'}
---------------------------
{'dia1': 'domingo', 'dia3': 'terça-feira', 'dia4': 'quarta-feira', 'dia5': 'quinta-feira'}
---------------------------
{'dia1': 'domingo', 'dia2': 'segunda-feira', 'dia3': 'terça-feira', 'dia4': 'quarta-feira', 'dia5': 'quinta-feira', 'dia6': 'sexta-feira', 'dia7': 'sábado'}
---------------------------
"""



# AULA 05 -----------FUNÇÕES COM DICIONÁRIOS---------------

dias_da_semana = {"dia1":"domingo", "dia2":"segunda-feira","dia3":"terça-feira","dia4":"quarta-feira","dia5":"quinta-feira","dia6":"sexta-feira","dia7":"sábado"}

print(dias_da_semana.popitem())
print(dias_da_semana.popitem())

del(dias_da_semana["dia2"])

print(dias_da_semana.keys())
print(dias_da_semana.values())

"""Execucao
('dia7', 'sábado')
('dia6', 'sexta-feira')
dict_keys(['dia1', 'dia3', 'dia4', 'dia5'])
dict_values(['domingo', 'terça-feira', 'quarta-feira', 'quinta-feira'])
{'dia1': 'domingo', 'dia3': 'terça-feira', 'dia4': 'quarta-feira', 'dia5': 'quinta-feira'}
"""