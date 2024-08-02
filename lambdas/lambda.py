"""
Lambda é uma maneira mais curta de uma função, como se fosse uma função anÔnima
"""

autores = ['davi feliciano', 'pedrin de cria', 'juninho do morro', 'flavin do pneu', 'cleito rasta', 'junior negao']
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)