"""
Conjuntos
    -Conjuntos em qualquer linguagem de programação é quando fazermos referência a teoria dos conjuntos
    -Aqui no python conjuntos são chamados de Sets

Dito isto, da mesma forma que na matemática:
    -Sets(conjuntos) não possuem valores duplicados;
    -Sets(conjuntos) não possuem valores ordenados;
    -Elementos não são acessados via indice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizadar quando precisamos armazenar elementos , mas não nos importamos com a
ordenação deles. Quando não precisamos nos preocupar com chaves, va,ores e itens duplicados.

Os conjuntos são referenciados em Python com chaves {}

Diferenã entre conjuntos e map em Python
    - Um dicionário tem chave/valor
    - Um conjuntos tem apelas valor

#Definindo conjuntos
#Forma não usual
s = set(1,2,3,4,5,6,1,1,1)
OBS: Ao se criar um conjuntos, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar
erro e não fará parte do conjunto.

#Forma mais comum
s = {1,2,3,4,5,1,1}

Para verificar se determinado elementos esta no conjunto:
for 1 in s:
    print('s')

#IMPORTANTE
Listas aceitam valores duplicados
Tuplas aceitam valores duplicados
Dicionários não aceitam chaves duplicadas
Conjuntos não aceitam valores duplicados

Podemos colocar diferentes tipos de dados nos conjuntos

Podemos iterar normalmente sobre os conjuntos
for c in conjuntos:
    print(c)

#METODOS
Adicionar conjuntos.add('Item desejado')
Remover conjuntos.remove('Item desejado') Se não encontrar o item gera erro
Remover conjuntos.discard('Item desejado') Se não encontrar o item gera não erro
Fazer uma copia conjuntos.copy()

Metodos na matemática
Uni dois conjuntos conjuntos2 = conjuntos.union('conjuntos1') ou |
Faz a intersecção conjuntos2 = conjuntos.intersection('conjuntos1') ou &
Faz a diferença conjuntos2 = conjuntos.difference('conjuntos1')
max,sum,min,len
"""