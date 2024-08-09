"""
Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo assim que o programa
pare de funcionar e o usuário receba mensagens de erro inesperadas.
"""
try:
    print('davi'[12])
except ValueError:
    print('O valor fornecido não é compatível')
except NameError as err:
    print(f'Deu NameError: {err}')
except:
    print('Este erro não foi previsto')