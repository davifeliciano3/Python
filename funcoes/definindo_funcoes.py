"""
A forma de uma função é dada por:
    def nome_da_funcao(parametros):
        bloco_funcao

nome_da_funcao -> Sempre, com letras minúsculas, e se for nome composto, separado por underline(Snake Case);
parametros -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece
Pode ter ou não retorno neste bloco

Sempre se utiliza a palavra reservada def para definir uma função
"""

#Em python, podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável
def canta_parabens():
    print("Canta parabens")

canta = canta_parabens

canta()