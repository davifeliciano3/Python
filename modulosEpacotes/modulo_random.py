"""
Modulos são arquivos em python que vc pode importar
Existe duas formas de importar módulos

1- import random- aqui voce vai importar todos os arquivos do modulo random deixando seu arquivos mais pesado
 Para acessar alguma coisa quando importa desta forma deve fazer random.(nome da função)

2- from random import random - aqui vc importar apenas a função, sendo assim a forma recomendada
 Para acessar a função é necessário apenas digitar o nome dela random()

3- import random as rdm Utilizando alias (apelidos) para módulos/funções

4- import random * Importando todas a função
    Para acessar apenas escreva o nome da função

5- from random import random as rmd Importando uma função com apelido

6- from random import random, randint .... vc pode importar mais de uma função e colocar apelido tmb
"""

from random import random
print(random) #Gera um números pseudo-aleatórios entre 0 e 1

from random import uniform
print(uniform(4,6))#Gera números pseudo-aleatórios entre valores estabelecidos é não inclusive

from random import randint
print(randint(1,61))#Gera números inteiros pseudo-aleatórios entre valores estabelecidos é não inclusive

from random import choice
jogadas = ['pedra','papel','tesoura']
print(choice(jogadas))#Mostra um valor aleatório entre um iterável

from random import shuffle
a = shuffle(jogadas) #Tem a função de embaralhar dados
print(a)

#Quando trabalhamos com muitos imports fazemos

from random import (
    random,
    randint,
    shuffle,
    choices
)
