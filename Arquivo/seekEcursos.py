"""
seel() -> é utiliado para movimentar o cursos pelo arquivo
"""

arquivo = open('texto.txt')
print(arquivo)

linhaAlinha = arquivo.readline()#le linha por linha
print(linhaAlinha)

stringLinha = arquivo.readlines()#devolve uma lista com as linhas como iteravel
print(stringLinha)

ler = arquivo.read()
print(ler)

#seel() recebe um parametro que indica onde queremos colocar o cursos
arquivo.seek(0)
print(ler)

print(arquivo.closed) #verifica se um arquivo esta aberto ou fechado 

#fechando o arquivo
arquivo.close()
