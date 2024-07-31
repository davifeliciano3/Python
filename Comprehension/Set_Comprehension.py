"""
Set comprehension conjuntos não tem valores repetidos
set = {1,2,3,4,5}
"""

numeros = {num for num in range(1,7)}
print(numeros)

numeros = {num ** 2 for num in range(1,10)}
print(numeros)

numeros = {num:num ** 2 for num in range(1,10)}
print(numeros)

letras = {letras for letras in 'davi feliciano oliveira de sousa'}
print(letras)