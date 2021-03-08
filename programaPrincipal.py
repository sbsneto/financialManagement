from menus import cabecalho, extratus, menuLancamento, menu_principal, menu_secundario
from tratarErros import leia_int, leia_str
from conta import Conta
from debitoCredito import DebitoCredito
from limpa_tela import limpa

import time
import os

repetir = True
while repetir == True:
    contaCliente: Conta
    dividas = []
    lançamentos = []
    extratoCompleto = []
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
        novaConta = DebitoCredito(saldo, "+", "NOVA CONTA", "")
        extratoCompleto.append(novaConta)
        limpa()
    elif op == 2:
        while True:
            cabecalho()
            menu_secundario()
            op2 = leia_int('Escolha a opção desejada: ')
            limpa()

            if (op2 == 1):

                cabecalho()
                descricao = str(input("Descrição do Debito: "))
                tipo = str("-")
                valor = float(input("Insira o valor do Debito: "))
                dataOp = str(input("Insira a data e a Hora da Operação: "))
                contaCliente.debito(valor)

                gasto = DebitoCredito(
                    valor, tipo.upper(), descricao.upper(), dataOp.upper())

                print(contaCliente.saldo)

                dividas.append(gasto)
                extratoCompleto.append(gasto)
                limpa()
            elif (op2 == 2):
                cabecalho()
                descricao = str(input("Descrição do Lançamentos: "))
                tipo = str("+")
                valor = float(input("Insira o valor do Lançamento: "))
                dataOp = str(input("Insira a data e a Hora da Operação: "))

                contaCliente.credito(valor)

                credito = DebitoCredito(
                    valor, tipo.upper(), descricao.upper(), dataOp.upper())

                lançamentos.append(credito)
                extratoCompleto.append(credito)
                limpa()
            elif (op2 == 3):
                limpa()
                break
            else:
                print("ERRO! Opção inválida ! ")
    elif op == 3:
        cabecalho()
        extratus()
        op3 = leia_int('Escolha a opção desejada: ')
        while True:
            if(op3 == 1):
                for a in range(len(extratoCompleto)):
                    print(
                        extratoCompleto[a].tipo,
                        extratoCompleto[a].descricao,
                        extratoCompleto[a].valor,
                        extratoCompleto[a].dataOperacao)
            elif(op3 == 2):
                for b in range(len(extratoCompleto)):
                    if(dividas[b].tipo == "-"):
                        print(
                            dividas[b].tipo,
                            dividas[b].descricao,
                            dividas[b].valor,
                            dividas[b].dataOperacao)
            elif(op3 == 3):
                for c in range(len(extratoCompleto)):
                    if(lançamentos[c].tipo == "-"):
                        print(
                            lançamentos[c].tipo,
                            lançamentos[c].descricao,
                            lançamentos[c].valor,
                            lançamentos[c].dataOperacao)
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
