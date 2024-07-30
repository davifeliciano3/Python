"""
Módulo Collections: Ordered Dict
#Em um dicionário padrão a ordem não é garantida
#Com o ordered Dict vc garante a ordem por insersão
"""
from collections import OrderedDict

#DICIONÁRIO PADRÃO
dic1 = {'a':1, 'b':2}
dic2 = {'b':2, 'a':1}
print(dic1 == dic2) #True Verdade


#DICIONÁRIO OrderedDict
dic1 = OrderedDict( {'a':1, 'b':2})
dic2 = OrderedDict({'b':2, 'a':1})
print(dic1 == dic2) #Falso pois converva a ordem de insersão 