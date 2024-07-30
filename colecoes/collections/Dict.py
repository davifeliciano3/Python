"""
Módulo de Collections - Default Dict
Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default, podendo utilizar um lamb
da para isso. Este valor será utilizado sempre que não houver um valor definido. Caso tentamos acessar uma
chave que não existe, essa chave será criada e o  valor default será attribuído

Se tentarsemos acessar uma chave não existente em um dicionário normal geraria um keyerror

OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores
"""

from  collections import defaultdict

dicionario = defaultdict(lambda :'valor padrão')
dicionario['Nome'] = 'Davi'
dicionario['Sobrenome']
print(dicionario)