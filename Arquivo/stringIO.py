"""
StringIO -> utilizado para ler e criar arquivos em memória
"""
from io import StringIO

mensagem = 'uma string'

#podemos criar um arquivo em memoria já com uma string inserida ou mesmo vazio para inserirmos um texto depois
arquivo = StringIO(mensagem)

#Agora tendo o arquivo, podemos utilizar tudo que já sabemos
print(arquivo.read())

#escrevendo outros textos
arquivo.write('siga em frente')

#podemos inclusive movimentar o cursor
arquivo.seek(0)
print(arquivo.read())