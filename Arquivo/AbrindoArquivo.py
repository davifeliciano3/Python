"""
Leitura de arquivo

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literalmente significa 'abrir'. Esta função possue parametros e vem por padrão r
open() é usada para manipular um aquivo

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

tipo de retorno _io.TextIOWrapper

open().read() retorna uma string
"""

texto = open('texto.txt')
print(texto)

ler = texto.read()
print(ler)