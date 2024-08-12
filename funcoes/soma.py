def soma(lista):
    soma = 0
    for numeros in lista:
        soma += numeros
    return soma


if __name__ == "__main__":
    print('Foi executado diretamente')
else:
    print(f"O pacote foi importado  :  {__name__}")