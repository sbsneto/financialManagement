def cabecalho():
    print("#" * 58)
    print("#" * 18, " Financial Manager ", "#" * 18)
    print("#" * 58)


def menu_principal():
    print("#" * 10, " 1 para Cadastrar Debitos ou Lançamentos!", "#" * 10)
    print("#" * 10, " 2 Consultar Extrato!", "#" * 8)
    print("#" * 10, " 3 para sair do sistema!", "#" * 21)


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
