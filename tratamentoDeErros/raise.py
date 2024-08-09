"""
Levantando os própios erros com raise

raise -> Lança exceções
OBS: Não é uma função. E uma palavra reservada, assim como def ou qualquer outra

útil para criar suas própias exceções e mensagens de erro.

Forma geral de utilização

raise TipoDoErro('Mensagem de erro')
raise finaliza a sessão quando ele é ativda
"""
def colore(texto,cor):
    if type(texto) is not str:
        raise TypeError("O Texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("Cor precisa ser uma string")
    print(f'O {texto} será impresso na cor {cor}')



def colore(texto,cor):
    cores = ('verde','amarelo','azul','branco')
    if type(texto) is not str:
        raise TypeError("O Texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("Cor precisa ser uma string")
    if cor not in cores:
        raise ValueError(f"A {cor} não é permitida")
    print(f'O {texto} será impresso na cor {cor}')