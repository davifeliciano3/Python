"""
1 - abrindo arquivo
2 - trabalhando com arquivo
3 - fechando arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco
with

"""

with open('texto.txt') as arquivo:
    print(arquivo.read())
    print(arquivo.closed)

print(arquivo.closed)
