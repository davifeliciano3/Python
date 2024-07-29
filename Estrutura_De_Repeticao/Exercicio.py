print("#####5 primeiros multiplo de 3########")

fim = False

while fim == False:
    for numeros in range(1,6):
        print(numeros *3 )
    fim = True

mensagem = ''

while mensagem != 'fim':
    for numero in range(10,-1,-1):
        print(numero)
    print('FIM')
    mensagem = 'fim'

inteiro = 0

while inteiro != 101_000:
    print(f'O valor é: {inteiro}')
    inteiro += 1000
