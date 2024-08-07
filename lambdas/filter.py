"""
Filter() -> Serve para filtrar dados de uma determinada coleção

No filtro eu seleciono os dados desejados, já no map eu transformo os dados. Um é como um if e o outro é como um for.
filter seleciona elementos com base em uma condição, map transforma elementos aplicando uma função a eles.
Ambos retornam iteradores, que geralmente são convertidos em listas para serem utilizados
"""
#A função de filter sempre vai retornar true ou false
#A função de map sempre vai retornar um valor
import statistics #importa a biblioteca statistics

dados = [1.2,3.2,3.2,5.5,4.8] #lista com dados

media = statistics.mean(dados) #Faz a média da lista dados
print(f'Média: {media}')

res = filter(lambda valor: valor > media, dados) #Faz o filtro da lista dados,
print(list(res))                                 # onde a condição é o número ser maior que a média


usuarios = [
    {'username':'Davi','tweet':['peixe','pão de batata']},
    {'username': 'Davi', 'tweet': ['peixe', 'pão de batata']},
    {'username': 'Carol', 'tweet': []}
]

usuarios_inativo = list(filter(lambda usuario: usuario['tweet'] != 0,usuarios))
print(usuarios_inativo)


#Utilizando filter e map

#Retorne uma lista contendo O nome da sua estrutora é {nome}, desde que o nome seja menor que 5

nomes = ['davi','pedro','ivanilde','ednaldo','soso','gabi']

nova_lista = list(map(lambda nome: f'Sua estrutora é {nome}',filter(lambda nome: len(nome) < 5,nomes)))
print(nova_lista)