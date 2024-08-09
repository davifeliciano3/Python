"""
Try/ execpt / else / finally

Dica de onde tratar o código -> TODA ENTRADA DO USUÁRIO DEVE SER TRATADA!
A FUNÇÃO DO USUÁRIO É DESTRUIR SEU SISTEMA
"""
num = 0
try:
    num = int(input("Informe um número: "))
except ValueError:
    print('Valor incorreto')
finally:
    print(f'Vc digitou {num}')



try:
    num = int(input("Informe um número: "))
except ValueError:
    print('Valor incorreto')
else: # é executa só se não ocorrer o erro
    print(f'Vc digitou {num}')



try:
    num = int(input("Informe um número: "))
except ValueError:
    print('Valor incorreto')
else: # é executa só se não ocorrer o erro
    print(f'Vc digitou {num}')
finally:
    print('Chegamos no finally')

#Finally geralmente é executado para fechar ou deslogar recursos

#Exemplo avançado

def dividir(a,b):
    try:
        return  int(a)/int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível fazer divisão por zero'


#Exemplo avançado generico

def dividir(a,b):
    try:
        return  int(a)/int(b)
    except :
        return 'Ocorreu um erro'

#Exemplo avançado semi-generico

def dividir(a,b):
    try:
        return  int(a)/int(b)
    except (ValueError,ZeroDivisionError) as err:
        return f'Ocorreu um erro {err}'
