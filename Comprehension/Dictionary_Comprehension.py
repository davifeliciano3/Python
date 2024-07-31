"""
Dicionary Comprehension

Pense:
{chave:valor for chave,valor in iteravel}
{valor:valor*2 for valor in iteravel}
"""
numeros = {'a':1,'b':2,'c':3,'d':4}
letras = {chave:valor  for chave,valor in numeros.items()}
print(letras)

print('##################################################')
numeros = {'a':1,'b':2,'c':3,'d':4}
quadrado = {valor:valor * 2 for chave,valor in numeros.items()}
print(quadrado)

print('##################################################')
numeros = {'a':1,'b':2,'c':3,'d':4}
quadrado = {valor:valor ** 2 for chave,valor in numeros.items()}
print(quadrado)

print('##################################################')
numeros = [1,2,3,4,5,6,7]
quadrado = {valor:valor ** 2 for valor in numeros}
print(quadrado)

print('##################################################')
chave = 'abcde'
valores = [1,2,3,4,5]
mistura = {chave[i]:valores[i] for i in range(0,len(chave))}
print(mistura)

print('##################################################')

numeros = [1,2,3,4,5,6,7,8,9,10]

res = {num:('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)