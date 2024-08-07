"""
DICIONÁRIOS

OBS: Em outras linguagens pode ser conhecido com map

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves {}

OBS: -Chave e valor são separados por dois pontos chave:valor
     - Tanto chave quanto valor podem ser de qualquer tipo de dado:
     - Podemos misturar tipos de dados;

#Criando um dicionário

Forma 1 - mais tradicional
paises = {'br':'Brasil','eua':'Estados unidos da america','py':'Paraguai'}

2 Forma
paises = dict(br='Brasil',eua='Estados unidos')

#Acessando valores

Forma 1 - Acessando via chave, da mesma forma que tupla
print(paises['br']

Forma 2 - Recomendado - Usando get
print(paises.get('br'))- se não achar retorana None

#podemos definir um valor padrão caso o get não encontre nada
print(paises.get('br','Não foi encontrado'))

#Verifica se uma chave esta em um dicionarios
'br' in paises

localidades = { # è bom usar tuplas como chaves, pois são imutaveis
    (3123,312312):'São paulo',
}

#Adicionando um elemento

receita = {'jan':100,'fev':120}
receita['set'] = 300

novo_dado = {'mai':400}
receita.update(novo_dado)

#Pode adicionar novos elementos e atulizar dados da mesma maneira
#Em dicionarios não podemos ter chaves repetidas- se houver ele atualiza

#Removendo elemetos

receita.pop('br') o valor do objeto é retornado
del receita['fev'] 

#fromkeys atribui chaves e elementos
#copy
"""