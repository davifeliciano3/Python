"""
PDB python debugger


"""
#pycharm
def dividir(a,b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        print(f'Erro: {err}')

print(dividir(3,2))

#PDB
#Importar a biblioteca pdb e usar função set_trace()
#A partir do python 3.7 não é preciso importar a biblioteca pdb, pois ela já vem integrada
#Cuidado com os comflitos entre nomes de variáveis e os comando do pdb
#Se tiver variavel com mesmo nome de um comando do pdb utiliza-se p e nome da variavel
#comandos
"""
l listar a onde estamos
n proxima linna 
p imprime variavel
c continua a execução é o fim 
"""
import pdb

nome = ' daiv '
sobrenome = ' feliciano '
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = ' python '
final = nome_completo + ' Faz o curso de ' + curso
print(final)




nome = ' daiv '
sobrenome = ' feliciano '
import pdb; pdb.set_trace() # o debug é utilizando durante o desenvolvimento e como todos os imports ficam no inicio
#Colocando aqui direto fica mais fácil de achalo para removelo no futuro
nome_completo = nome + ' ' + sobrenome
curso = ' python '
final = nome_completo + ' Faz o curso de ' + curso
print(final)