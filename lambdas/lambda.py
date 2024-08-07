"""
Lambda é uma maneira mais curta de uma função, como se fosse uma função anÔnima
Expressões lambda (às vezes chamadas de funções lambda) são usadas para criar funções anônimas.
A expressão lambda parameters: expression produz um objeto função.
 O objeto sem nome se comporta como um objeto de função definido com:

 Mais utilizada para ordenação de dados
"""

autores = ['davi feliciano', 'pedrin de cria', 'juninho do morro', 'flavin do pneu', 'cleito rasta', 'junior negao']
autores.sort(key=lambda nome: nome.split(' ')[-1].upper())
print(autores)

def geradora_quadratica(a,b,c):
    return lambda x:a*x ** 2 + b * x + c

teste = geradora_quadratica(1,2,3)
print(teste(4))