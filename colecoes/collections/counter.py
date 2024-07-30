"""
Módulo Collections - Counter (Contador)

Collections -> High-performace Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo collections counter que é parecido com
um dicionário, contendo como chave o elemento da lista passada como parârametro e como valor a quantidade de
ocorrências desse elemento

from collections import Counter

lista = [1,2,3,4,4,4,4,4,4,2,2,2]
res = Counter(lista) Vai mostar a quantidade de ocorrências de cada elementos
res.most_common(2) vai mostar os dois itens mais comuns 
"""