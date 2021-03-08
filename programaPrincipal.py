from menus import cabecalho, menuLancamento, menu_principal, menu_secundario, extratus
from tratarErros import leia_int, leia_str
from conta import Conta
from debitoCredito import DebitoCredito
from limpa_tela import limpa

import time
import os

dividas = []
lançamentos = []
extratoCompleto = []

repetir = True
while repetir == True:
    contaCliente: Conta
    cabecalho()
    menu_principal()
    op = leia_int('Escolha a opção desejada: ')
    limpa()
    if op == 1:
        cabecalho()
        nomeCliente = leia_str("Insira o nome do Cliente: ")
        numConta = leia_int("Insira o número da conta: ")
        saldo = float(input("Insira o saldo atual da conta: "))
        contaCliente = Conta(numConta, nomeCliente, saldo, "")
        lançamentos.append(contaCliente)
        limpa()
    elif op == 2:
        while True:
            cabecalho()
            menu_secundario()
            op2 = leia_int('Escolha a opção desejada: ')
            limpa()

            if (op2 == 1):
                descricao = str(input("Descrição do Debito: "))
                tipo = str("-")
                valor = float(input("Insira o valor do Debito: "))
                dataOp = str(input("Insira a data e a Hora da Operação: "))

                contaCliente.debito(valor)

                gasto = DebitoCredito(
                    valor, tipo.upper(), descricao.upper(), dataOp.upper())

                dividas.append(gasto)
                extratoCompleto.append(gasto)
                print(len(extratoCompleto))
                limpa()
            elif (op2 == 2):
                descricao = str(input("Descrição do Lançamentos: "))
                tipo = str("+")
                valor = float(input("Insira o valor do Lançamento: "))
                dataOp = str(input("Insira a data e a Hora da Operação: "))

                contaCliente.credito(valor)

                credito = DebitoCredito(
                    valor, tipo.upper(), descricao.upper(), dataOp.upper())

                lançamentos.append(credito)
                extratoCompleto.append(credito)
                print(len(extratoCompleto))
                limpa()
            elif (op2 == 3):
                limpa()
                break
            else:
                print("ERRO! Opção inválida ! ")
    elif op == 3:
        while True:
            extratus()
            op3 = leia_int('Escolha a opção desejada: ')
            if(op3 == 1):
                i = 0
                print(len(extratoCompleto))
                while i < len(extratoCompleto):
                    print(
                        extratoCompleto[i].tipo,
                        extratoCompleto[i].descricao,
                        extratoCompleto[i].valor,
                        extratoCompleto[i].dataOperacao)
                    i += 1
                # break
            elif(op3 == 2):
                i = 0
                len(dividas)
                while i < len(dividas):
                    print(
                        dividas[i].tipo,
                        dividas[i].descricao,
                        dividas[i].valor,
                        dividas[i].dataOperacao)
                    i += 1
                # break
            elif(op3 == 3):
                i = 0
                print(len(lançamentos))
                while i < len(lançamentos):
                    print(
                        lançamentos[i].tipo,
                        lançamentos[i].descricao,
                        lançamentos[i].valor,
                        lançamentos[i].dataOperacao)
                    i += 1
                # break
            elif(op3 == 4):
                limpa()
                break
            else:
                print("ERRO! Opção inválida ! ")
    elif op == 4:
        repetir = False
    elif op == 5:
        break
    else:
        print("Erro olhar um valor entre 1 e 4")
