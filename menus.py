def cabecalho():
    print("#" * 58)
    print("#" * 18, " Financial Manager ", "#" * 18)
    print("#" * 58)


def menu_principal():
    print("#" * 10, " 1 Cadastrar Conta: !", "#" * 8)
    print("#" * 10, " 2 para Cadastrar Debitos ou Lançamentos!", "#" * 10)
    print("#" * 10, " 3 Consultar Extrato!", "#" * 8)
    print("#" * 10, " 4 Consultar Saldo atual da Conta!", "#" * 8)
    print("#" * 10, " 5 para sair do sistema!", "#" * 21)


def menu_secundario():
    print('Digite 1 para cadastrar Debito!')
    print('Digite 2 para cadastrar lançamentos!')
    print('Digite 3 para voltar para o menu principal!')


def extratus():
    print('Digite 1 para Consultar Extrato Completo!')
    print('Digite 2 para Consultar Extrato dos debitos!')
    print('Digite 3 para Consultar Extrato dos Lançamentos!')
    print('Digite 4 para voltar ao Menu Principal! ')
