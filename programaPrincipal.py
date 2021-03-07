from menus import cabecalho, menuLancamento, menu_secundario, menu_principal, consultas
from tratarErros import leia_int, leia_str
from conta import Conta
import time
from limpa_tela import limpa

while True:
    financeiro = []
    cabecalho()
    menu_principal()
    opcaoMenuPrincipal = leia_int('Escolha a opção desejada: ')
    limpa()
    if opcaoMenuPrincipal == 1:
        while True:
            cabecalho()
            menuLancamento()
            #menu_secundario()
            opcaoMenuSecundario = leia_int('Escolha a opção desejada: ')
            conta = Conta
            if (opcaoMenuSecundario == 1):
                cabecalho()
                descricao = str("Descrição do Debito: ")
                debito = float("Insira o valor do Debito: ")

                conta.setDescricao(descricao)
                conta.setSaldo(debito)
                print(conta.getDescricao(), conta.getSaldo())
                # financeiro.append(conta)
                # print(financeiro)
            elif (opcaoMenuSecundario == 2):
                limpa()
            elif (opcaoMenuSecundario == 3):
                limpa()
                cabecalho()
                menu_principal()
            else:
                limpa()
                cabecalho()
                print("\n ",opcaoMenuSecundario," não está entre as opções.\n")
                menu_secundario()
    elif opcaoMenuPrincipal == 2:
        print('Opção 2 selecionada')
    elif opcaoMenuPrincipal == 3:
        print('Opção 3 selecionada')
    elif opcaoMenuPrincipal == 4:
        print('Opção 3 selecionada')
    elif opcaoMenuPrincipal == 5:
        break
