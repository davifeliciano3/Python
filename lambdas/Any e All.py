"""
All -> Retorna true se todos os elementos do iteravel são verdadeiros ou ainda se o iterável está vazio
"""
print(all([0,1,3,4,5,4])) #False
print(all([1,3,4,5,4])) #True
print(all([])) #True

nomes = ['Carlos','Camila','Carla','Cassiano','Cristina','Roberto']
print(all([nome[0]=='C' for nome in nomes]))

"""
Any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
"""

nomes = ['Carlos','Camila','Carla','Cassiano','Cristina','Roberto']
print(any([nome[0]=='C' for nome in nomes]))