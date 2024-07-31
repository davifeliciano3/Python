"""
Listas aninhadas (Nested Lists)

- Algumas linguagens de programação C/java possuem uma estrutura de dado chamada de array
    -Unidimensionais (Arrays/Vetores)
    -Multidimensionais (Matrizes)

lista = [[1,2,3],[3,2,1]]
print(lista[0][0])

for lista in listas:#Pegando cada linha
    for numero in lista:#Pegando cada coluna
        print(numero)
"""

listas = [[1,2,3],[3,2,1]]

[print(numero) for numero in listas] #Pegando linhas
print('##########')
[[print(numero) for numero in lista]  for lista in listas]
print('##########')
listaRage = [[colunas for colunas in range(2)] for linhas in range(5)]
print(listaRage)