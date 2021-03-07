from menus import cabecalho, menu_secundario, menu_principal, consultas
from tratarErros import leia_int, leia_str
from conta import Conta
import time
from limpa_tela import limpa

while True:
    financeiro = []
    cabecalho()
    menu_principal()
    op = leia_int('Escolha a opção desejada: ')
    limpa()
    if op == 1:
        while True:
            cabecalho()
            menu_secundario()
            op2 = leia_int('Escolha a opção desejada: ')
            conta = Conta
            if (op2 == 1):
                cabecalho()
                descricao = str("Descrição do Debito: ")
                debito = float("Insira o valor do Debito: ")

                conta.setDescricao(descricao)
                conta.setSaldo(debito)
                print(conta.getDescricao(), conta.getSaldo())
                # financeiro.append(conta)
                # print(financeiro)
            elif (op2 == 2):
                limpa()
            elif (op2 == 3):
                limpa()
                break
            else:
                print("ERRO! Opção invalida ! ")
    elif op == 2:
        print('Opção 2 selecionada')
    elif op == 3:
        print('Opção 3 selecionada')
    elif op == 4:
        print('Opção 3 selecionada')
    elif op == 5:
        break
