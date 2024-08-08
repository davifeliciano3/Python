"""
A função zip() em Python é usada para combinar elementos de iteráveis (como listas, tuplas, etc.) em pares,
criando um iterador que gera tuplas com elementos correspondentes de cada iterável fornecido.
Quando os iteráveis possuem tamanhos diferentes, o zip() para quando o menor iterável é esgotado.
"""

nomes = ['Ana', 'Bruno', 'Carla']
idades = [25, 30, 22]

pares = zip(nomes, idades)
for nome, idade in pares:
    print(f"{nome} tem {idade} anos.")





nomes = ['Ana', 'Bruno', 'Carla']
idades = [25, 30, 22]
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']

dados = zip(nomes, idades, cidades)
for nome, idade, cidade in dados:
    print(f"{nome}, {idade} anos, mora em {cidade}.")






dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
vendas_produto_a = [3, 2, 4]  # faltam dados para 'Quinta' e 'Sexta'
vendas_produto_b = [1, 0, 5, 3, 4]

# Sincronizar vendas para os dois produtos (parar quando a menor lista for esgotada)
sincronizado = zip(dias, vendas_produto_a, vendas_produto_b)
for dia, venda_a, venda_b in sincronizado:
    print(f"No dia {dia}, vendas do Produto A: {venda_a}, Produto B: {venda_b}")
