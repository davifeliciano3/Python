"""
Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler.

Para escrevermos em um arquivo, após abrir o arquivo utilizamos a função write()
Essa função recebe uma string com parametros

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado, caso
ele já exista, o anterior será apagado e um novo será criado. Dessa forma, todo o conteúdo no arquivo
anterior é perdido
"""

with open('novo.txt', 'w') as arquivo:
    arquivo.write('davi é lindo')

