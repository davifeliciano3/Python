nome = 'Davi Feliciano'

for letras in nome:
    print(letras)

for numero in range(1,10):# range é não inclusive
    print(numero)

for indice, valor in enumerate(nome):
    print(f'Este é o indice: {indice} Este é o valor: {valor}')

for _, valor in enumerate(nome):
    print(f'Este é o indice:  Este é o valor: {valor}')

