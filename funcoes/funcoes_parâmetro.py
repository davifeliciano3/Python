"""
Parametros são variáveis declaradas na definição de uma função
Argumentos são dados passados durante a execução de uma função

Nomeando parametros com Keyword Arguments
"""
def nome_completo(nome,sobrenome):
    return nome + sobrenome

normal = nome_completo('davi', 'feliciano')
print(normal)
Keyword = nome_completo(sobrenome='Feliciani',nome='Davi')
print(Keyword)