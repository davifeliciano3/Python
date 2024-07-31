"""
Crie um programa que tenha uma função que recebe um parâmetro inteiro e devolve o seu dobro.
def dobro(num):
    return num * 2
"""""


"""
Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e
imprima ela por extenso como “1 de janeiro de 2204”.

"""



def converte_dada(data):
    mes = ''
    if data[3:5] == '01':
        mes = 'janeiro'
    elif data[3:5] == '02':
        mes = 'fevereiro'
    elif data[3:5] == '03':
        mes = 'março'
    elif data[3:5] == '04':
        mes = 'abril'
    elif data[3:5] == '05':
        mes = 'maio'
    elif data[3:5] == '06':
        mes = 'junho'
    elif data[3:5] == '07':
        mes = 'julho'
    elif data[3:5] == '08':
        mes = 'agosto'
    elif data[3:5] == '09':
        mes = 'setembro'
    elif data[3:5] == '10':
        mes = 'outubro'
    elif data[3:5] == '11':
        mes = 'novembro'
    elif data[3:5] == '12':
        mes = 'desembro'

    dia = ''
    if data[0:2] == '01':
        dia = '1'
    elif data[0:2] == '02':
        dia = '2'
    elif data[0:2] == '03':
        dia = '3'
    elif data[0:2] == '04':
        dia = '4'
    elif data[0:2] == '05':
        dia = '5'
    elif data[0:2] == '06':
        dia = '6'
    elif data[0:2] == '07':
        dia = '7'
    elif data[0:2] == '08':
        dia = '8'
    elif data[0:2] == '09':
        dia = '9'
    else:
        dia = data[0:2]
    ano = data[6:10]

    return f'{dia} de {mes} de {ano}'

data = '10/05/2024'
data_convertida = converte_dada(data)
print(data_convertida)

"""
Faça um programa que tenha uma função que receba uma lista de inteiros e retorne o maior valor
"""

def O_maior_da_lista(lista):
    return max(lista)

lista = [10000,32,43,123,3123,656]

maior = O_maior_da_lista(lista)
print(maior)
