def cabecalho():
    print("#" * 58)
    print("#" * 18, " Financial Manager ", "#" * 18)
    print("#" * 58)


def menu_principal():
    print('\n')
    print(" 1. Lançar Débitos ou Créditos")
    print(" 2. Consultar Saldo")
    print(" 3. Consultar Extrato")
    print(" 4. Consultar Saldo atual da Conta")
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


def extratus():
    print('Digite 1 para Consultar Extrato Completo!')
    print('Digite 2 para Consultar Extrato dos debitos!')
    print('Digite 3 para Consultar Extrato dos Lançamentos!')
    print('Digite 4 para voltar ao Menu Principal! ')
