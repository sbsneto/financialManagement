def cabecalho():
    print("#" * 58)
    print("#" * 18, " Financial Manager ", "#" * 18)
    print("#" * 58)


def menu_principal():
    print('\n')
    print(" 1. Lançar Débitos ou Créditos")
    print(" 2. Consultar Saldo")
    #print('\n')
    print("\n 0. Sair\n\n")

def menuLancamento():
    print(" 1. Debitar")
    print(" 2. Creditar")
    print(" 3. Voltar")
    print('\n')
    print(" 0. Sair")


def menu_secundario():
    print('Digite 1 para cadastrar Debito!')
    print('Digite 2 para cadastrar lançamentos!')
    print('Digite 3 para voltar para o menu principal!')


def consultas():
    print('Digite 1 para Mesas Com Pedidos em Aberto!')
    print('Digite 2 para Mesas Com Pedidos Pronto P/ Entrega!')
    print('Digite 3 para Mesas Com Pedidos Entregues!')
    print('Digite 4 para Mostrar o Status de todos os Pedidos! ')
    print('Digite 5 para Mostrar os Pedidos já pago ! ')
    print('Digite 6 para voltar! ')
