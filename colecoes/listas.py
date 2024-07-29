"""
Em Python as listas são:

    -Dinâmico: Não possuem tamanho fixo; ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
    -Qualquer tipo de dado: Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []

#Podemos facilmente checar se determinado valor está contido na lista
if 7 in lista:
    print("Esta na lista")

#Para ordenar uma lista utiliza-se sort() lista.sort()

#Para contar a quantidade de ocorrência de um número/letra em uma lista utiliza-se count(2) lista.count(10)

#Para adicionar elementos em uma lista utiliza-se append("Elemento que vai ser adicionado") lista.append(3)
lista.append([2,3,4,5]) vai adicionar uma lista

#Para adicionar uma lista dentro de uma lista utiliza-se extends lista.extends([1,3,4,5]) adiciona cada elemento individualmente

#Para adicionar elemento em um index específico utiliza-se lista.insert('index','valor')
Vai adicionar e jogar o elemento que esta no index desejado para frente

#Para juntar duas listas lista3 = lista + lista1 ou lista = lista.extends(lista1)

#Para inverter uma lista utiliza-se lista.reverse()

#Para remover o ultimo elemento utilize lista.pop(). O pop retorna o elemento que foi removido
    para remover de um index espefícico lista.pop('index')

#Para limpar uma lista utiliza-se lista.clear()

#Para fazer uma cópia da lista utiliza-se lista.copy()

#Para remover um valor utilizando o index utilize a função del del lista[0:2] 

Usando listas como pilhas -ULTIMO A ENTRAR É O PRIMEIRO A SAIR- pense em uma pilha de pratos
    lista.append() para adicionar e lista.pop()

Usando listar como filas -PRIMEIRO A ENTRAR É O PRIMEIRO A SAIR- pense em uma fila de um banco
    usar lista.inserts() para adicionar e lista.pop() pode não ser tão eficiente já que todos os elementos serão deslocados
    Para ter uma melhor eficiência utilize collections.deque-from collections import deque- com os metodos append() e popleft()


matrix = [
    [1,2,3],
    [3,2,1]
]


print([[linha[i] for linha in matrix] for i in range(3)])

Matriz Original (matrix):

Suponha que matrix seja uma lista de listas (uma matriz). Por exemplo
Compreensão Interna ([linha[i] for linha in matrix]):

Esta parte percorre cada linha da matriz (for linha in matrix).
Para cada linha, ela extrai o elemento na posição i (linha[i]).
Isso cria uma nova lista contendo os elementos na coluna i de todas as linhas.
Compreensão Externa ([[linha[i] for linha in matrix] for i in range(3)]):

Esta parte percorre os índices i de 0 a 2 (for i in range(3)), assumindo que a matriz tem exatamente 3 colunas.
Para cada valor de i, ela executa a compreensão interna [linha[i] for linha in matrix], que cria uma lista dos elementos na i-ésima coluna.


lista.slice() Separa os elementos

curso = ' '.join(lista) Pega uma lista e adiciona ' ' entra cada elemento/palavra

Para interar sobre uma lista faça
for numeros in lista_numeros:
    print(numeros) #vai joga o primeiro valor de lista_numeros em numeros, depois imprime e repete esse ciclo até acaba

# Gerando indice com for

for j,i in enumerate(lista): #enumerate gera pares de chave e valor
    print(j,i)

#Para acha um valor pelo indece use lista.index('valor desejado') retorna o primeiro valor a ser encontrada
    pode colocar da onde começar a procurar lista.index('valor desejado','da onde vai começar a procurar')
    pode buscar dentro de um range específico lista.index('valor','inicio','fim')

# slice() lista[inicio:fim:passe]

# sum() max() len() min()

# lista para tupla tupla = tuple(lista)

#Copiando uma lista para outra
    DEEP COPY- utiliza copy() e faz com que as listas sejam independestes

lista = [1,2,3]
nova = lista.copy() cria uma nova lista

nova.append(4)
print(lista)
print(nova)

SHALLOW COPY- listas são dependentes

lista = [1,2,3]
nova = lista

nova.append(4)
print(lista)
print(nova)

"""

