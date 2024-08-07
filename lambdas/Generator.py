from sys import getsizeof

#Gerando uma lista com list comprehension
list_comp = getsizeof([x*10 for x in range(10)])
print(list_comp)
#Gerando uma lista com set comprehension
list_set = getsizeof({x*10 for x in range(10)})
print(list_set)
#Gerando uma lista com Dicionary comprehension
list_Dicionary = getsizeof({x:x*10 for x in range(10)})
print(list_Dicionary)
#Gerando uma lista com Generator comprehension
list_Generator = getsizeof(x*10 for x in range(10))
print(list_Generator)