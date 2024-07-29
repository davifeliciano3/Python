numero: int = int(input("Digite um número"))
numero2: int = int(input("Digite outro número"))

if numero > numero2:
    print(f'O número {numero} é o maior')
else:
    print(f'O número {numero2} é o maior')

positivo: int = int(input("Digite um número"))

if positivo > 0:
    print(positivo * positivo)
else:
    print("Número inválido, digite um número positivo")


par: int = int(input("Digite um número e descubra se ele é par"))

if par % 2 ==0:
    print(f'O número {par} é par')
else:
    print(f'O número {par} é negativo')
