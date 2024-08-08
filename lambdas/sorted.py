"""
Sorted
OBS: Não é a mesma coisa que sort
ele não altera a lista propriamente dita apenas retorna ela de maneira ordenada
"""

numeros = [1,5,32,2,8]
print(sorted(numeros))

"""
parametros de sorted
"""
print(sorted(numeros,reverse=True))

usuarios = [
    {'nome':'davi','Cor':'azul'},
    {'nome': 'ivi', 'Cor': 'preta'},
    {'nome': 'pedro', 'Cor': 'rosa'},
    {'nome': 'ana', 'Cor': 'branca'},
]

print(sorted(usuarios, key= lambda usuarios:usuarios['nome']))