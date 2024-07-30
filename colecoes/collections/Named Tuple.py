"""
Módulo Collections - Named Tuple

#Recap tupla
tupla = 1,2,3

Named Tuple São tupla, diferenciadas, onde, especificamos um nome para a mesma e também parâmetros
"""
from collections import namedtuple
cachorro = namedtuple('Cachorro',['idade','raca','nome'])
ray = cachorro(8,'pinsher','aninha')
print(ray)
print(ray.nome)
print(ray[1])
print(ray.index('aninha'))
print(ray.count(8))
