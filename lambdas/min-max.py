"""
Max-Retorna o maior valor em um iterável ou o maior de dois elementos
"""
lista = [1,3,4,2,1,3,100]
print(max(lista))
print(max(0,2))

"""
Min- Retorna o menor valor de um iterável ou entre dois números
"""

print(min(lista))
print(min(0,2))

"""
Ao compara por strings ele usa a ordem alfabetica
"""

nomes = ['davi','sousa','feleciano','ana','vitoria']
print(max(nomes))
print(min(nomes))

#Comparando pelo tamanho

print(max(nomes,key= lambda nome:len(nome)))
print(min(nomes,key= lambda nome:len(nome)))