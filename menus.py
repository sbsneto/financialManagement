def cabecalho():
    print("#" * 58)
    print("#" * 17, " Financial Management ", "#" * 17)
    print("#" * 58)


def menu_principal():
    print('\n')
    print(" 1. Cadastrar uma Conta")
    print(" 2. Lançar Débitos ou Créditos")
    print(" 3. Consultar Extrato")
    print(" 4. Editar ou Excluir lançamento")
    print(" 5. Consultar Saldo Atual da Conta")
    print(" 6. logs")
    print("\n 0. Sair\n\n")


def menuLancamento():
    print(" 1. Debitar")
    print(" 2. Creditar")
    print(" 3. Voltar")
    print('\n')
    print(" 0. Sair")
    print(" ")


def menu_secundario():
    print(" 1. Cadastrar Débito")
    print(" 2. Cadastrar Crédito")
    print("\n")
    print(" 0. Voltar")


def extratos():
    print(" 1. Extrato Completo")
    print(" 2. Extrato dos Débitos")
    print(" 3. Extrato dos Créditos")
    print("\n")
    print(" 0. Voltar")
    print(" ")


def editarExcluir():
    print(" 1. Editar um lançamento")
    print(" 2. Excluir um lançamento")
    print("\n")
    print(" 0. Voltar")
    print(" ")
