"""
Reduce

OBS: A partir do Python3+ a função reduce() não é mais uma função integrada (built-in). Agora temos que importar
e utilizar esta função a partir do módulo 'functools'

Guido van Rossun: Utilize a função reduce() se voçê realmente precisa dela. Em todo caso, 99% das vezes
um loop for é mais legível

Entendendo reduce()


A função reduce recebe uma função que tem dois parâmetros

Na primeira execução  ela pega o primeiro e segundo para parametros e trabalaha com eles
A partir da segunda ela já pega o resultado antetior e trabalha com eles
"""
from functools import reduce

dados = [2,3,4,5,6,7,8,9]

# Para utilizar o reduce() nós precisamos de uma função que receba dois parâmetros

multi = lambda x , y: x * y

res = reduce(multi,dados)
print(res)