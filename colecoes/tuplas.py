"""
TUPLAS (tuple)

Tuplas são bastantes parecidas com listas
Existem duas diferenças entre tuplas e listas

1- As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação em uma tupla gera uma nova tupla
2- As tupas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação em uma tupla gera uma nova tupla

#CUIDADO 1: As tuplas são representadas por (), mas veja:
é tupla tupla = (1,23,4,3,2)
Não é tupla tupla = (1)
é tupla tupla = 1,23,4,3,2
é tupla tupla = (1,)

Nota-se que o faz ser uma tupla não é o parentese, mas sim a virgura ,,,,

# é possível fazer desestruturação e estruturação com tuplas
# métodos de adição e remoção não existem, pois as tuplas são imutaveis

#max sum min len funcionam desde que os elementos sejam do mesmo tipo

#Existe concatenação de tupla- desde que repeitem a caracteristica das tuplas serem imutaveis
tupla1 = 2,3,4,5,
tupla2 = 5,6,7,8,8
tupla 3 = tupla1 + tupla2

#tuplas são imutaveis, mas podemos sobrescrever seus valores
tupla1 = 1,2,3,4
tupla2 = 5,6,7,8

tupla1 = tupla1 + tupla2

#Interando sobre uma tupla

tupla = 1,2,3,4,5

for n in tupla:
    print(n)

for j,n in enumerate(tupla):
    print(j,n)

i = 0
while i < len(tupla):
    print(tupla[i])
    i++

#methodos que existem em lista e em tuplas
count e index len contains

#Tuplas são mais rápidas e mais seguras
"""