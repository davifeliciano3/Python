"""
List Comprehension

-Utilizando list Comprehension  nós podemos gerar novas listas com dados processados a partir de outro
iteravel

[dado for dado in iteravel]

numeros [1,2,3,4,5,6,7,8,9]

res = [numero *10 for numero in numeros]
-A primeira parte: for numero in numeros
-A segunda parte: numero * 10


"""
def dobra(num):
    return  num * 2

lista = [1,2,3,4,5,6,7,8,9,10]
lista_dobro = [dobra(numero) for numero in lista]
print(lista)
print(lista_dobro)

lista_dobro.clear()
for numero in lista:
    res = dobra(numero)
    lista_dobro.append(res)
print(lista_dobro)