from menus import cabecalho, menu_secundario, menu_principal, consultas
from tratarErros import leia_int, leia_str
from conta import Conta
import time
import os

while True:
    financeiro = []
    cabecalho()
    menu_principal()
    op = leia_int('Escolha a opção desejada: ')
    os.system("cls")
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

                # os.system("cls")
            elif (op2 == 2):
                os.system("cls")
            elif (op2 == 3):
                os.system("cls")
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
