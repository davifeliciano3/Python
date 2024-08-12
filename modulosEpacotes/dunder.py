"""
dunder name e dunder main

Em python, são utilizados dunder para criar funções, atributos, propriedades e etc utilizando double under para
não gerar conflito com os nomes desses elementos na programação

Cada arquivo .py tem seu __name__ e dentro do name tem o __main__ que é o arquivo principal
O __name__ só é o mesmo do __main__ se forem executados diretamente

se for executado por importação o nome dele será o mesmo do aqrquivo
"""
from funcoes.soma import soma
lista = [3,4,5,2,3]
print(soma(lista))
