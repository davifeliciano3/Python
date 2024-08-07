"""
MAP
"""

import math
def area(r):
    return math.pi * (r **2 )

#Sem map
raio = [32,21,3,1,11]
larea = []
for r in raio:
    larea.append(area(r))

print(larea)

#Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável. Retorna um Map object
#Apos ser utilizado o resultado é zerado
#Utilizando map

mapArea = map(area,raio)
print(mapArea)

for r in mapArea:
    print(r)

#Map com lambda

lareas = map(lambda r: math.pi * (r**2),raio)
print(lareas)
# f(r1)  f(r2) f(r3) f(r4)

for r in lareas:
    print(r)


#Outro exemplo

cidades = [('DF',20),('MT',30),('TO',10)]

c_para_f = lambda dado: (dado[0], 9/5 * dado[1] + 32)

convertentado = map(c_para_f,cidades)
for convetido in convertentado:
    print(convetido)


raio = [32,21,3,1,11] #lista com raio
areas = map(lambda r: math.pi * (r**2),raio) #calcula a área
print(list(areas))