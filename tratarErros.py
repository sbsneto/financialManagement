def leia_int(valor):  # função para tratamento de erros para inserção de valores inteiros
    while True:
        try:
            n = int(input(valor))
        except (ValueError, TypeError,):
            print('ERROR! POR FAVOR INSIRA UM NÚMERO INTEIRO VALIDO')
            continue
        else:
            return n


def leia_str(valor):  # função para tratamento de erros para inserção de valores caracteris
    while True:
        try:
            n = str(input(valor))
        except (ValueError, TypeError,):
            print('ERROR! POR FAVOR INSIRA APENAS CARÁTER')
            continue
        else:
            return n