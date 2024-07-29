numero = 2 #escopo global

if numero < 1:
    novo = numero + 1
    print(novo) #novo é uma variável local

numero: int = int(input("Digite um número"))
print(f'O número que vc digitou foi: {numero}')

numero1 = int(input("Digite um número  "))

numero2 = int(input("Digite outro número"))

numero3 = int(input("Digite outro número"))

print(f'A soma dos números digitados é: {numero1 + numero2 + numero3}')

print("Digite 3 números para ter a soma dos seus quadrados")

numero1 = int(input("Digite um número  "))

numero2 = int(input("Digite outro número"))

numero3 = int(input("Digite outro número"))

resultado = (numero1 * numero1) + (numero2 * numero2) + (numero3 * numero3)
print(f'A soma dos números digitados é: {resultado}')
