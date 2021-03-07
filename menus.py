def cabecalho():
    print("#" * 52)
    print("#" * 16, " Financial Manager ", "#" * 16)
    print("#" * 52)


def menu_principal():
    print("#" * 10, " 1 para Cadastrar Debito ou Credito!", "#" * 10)
    print("#" * 10, " 2 para Inserir Credito!", "#" * 5)
    print("#" * 10, " 3 Consultar Extrato!", "#" * 8)
    print("#" * 10, " 4 para sair do sistema!", "#" * 21)


def menu_secundario():
    print('Digite 1 para cadastrar Debito!')
    print('Digite 1 para cadastrar Credito!')
    print('Digite 2 para voltar para o menu principal!')


def consultas():
    print('Digite 1 para Mesas Com Pedidos em Aberto!')
    print('Digite 2 para Mesas Com Pedidos Pronto P/ Entrega!')
    print('Digite 3 para Mesas Com Pedidos Entregues!')
    print('Digite 4 para Mostrar o Status de todos os Pedidos! ')
    print('Digite 5 para Mostrar os Pedidos já pago ! ')
    print('Digite 6 para voltar! ')
