"""
fim = 0
lista = []
while fim < 6:
    numero = input("Digite um número que será adicionado em uma lista")
    lista.append(numero)
    fim += 1

print(lista)
"""

"""
listaA = []
listaA.append(1)
listaA.append(0)
listaA.append(5)
listaA.append(-2)
listaA.append(-5)
listaA.append(7)
print(listaA)

soma = listaA[0] + listaA[1] + listaA[5]
print(soma)

listaA.insert(5,100)
print(listaA)

for numeros in listaA:
    print(numeros)
"""

sair = 0
pares = 0
lista = []
contador = 0
listaPares = []
while sair < 10:
    numeros = int(input("Digite um número"))
    lista.append(numeros)
    if numeros % 2 == 0:
        contador += 1
        listaPares.append(numeros)
    sair += 1

print(f'Lista de números apresentada: {lista}')
print(f'Lista de números pares: {listaPares}')
print(f'Quantidade de números pares: {contador}')
