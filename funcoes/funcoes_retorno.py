"""
Usa-se return quando a função deve devolver um valor e o mesmo deve ser colocado em uma variável para ser
utilizado

1- Return finaliza a execução da função, ou seja, ela sai da função
2- Podemos ter, em uma função, diferentes returns;
3- Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores
"""
#Codificação desnecessária

def eh_impar():
    if 3 % 2 != 0:
        return 'impar'
    return 'par'
