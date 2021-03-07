from menus import cabecalho, extratus, menu_principal, menu_secundario
from tratarErros import leia_int, leia_str, leia_float
from conta import Conta
from debitoCredito import DebitoCredito

import time
import os
import random

repetir = True
while repetir == True:
    contaCliente: Conta
    dividas = []
    lançamentos = []
    extratoCompleto = []
    cabecalho()
    menu_principal()
    op = leia_int('Escolha a opção desejada: ')
    os.system("cls")
    if op == 1:
        cabecalho()
        nomeCliente = leia_str("Insira o nome do Cliente: ")
        numConta = leia_int("Insira o número da conta: ")
        saldo = float(input("Insira o saldo atual da conta: "))
        contaCliente = Conta(numConta, nomeCliente, saldo, "")
        lançamentos.append(contaCliente)
        os.system("cls")
    elif op == 2:
        while True:
            cabecalho()
            menu_secundario()
            op2 = leia_int('Escolha a opção desejada: ')
            os.system("cls")

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

                os.system("cls")
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
                os.system("cls")
            elif (op2 == 3):
                os.system("cls")
                break
            else:
                print("ERRO! Opção invalida ! ")
    elif op == 3:
        cabecalho()
        extratus()
        op3 = leia_int('Escolha a opção desejada: ')
        while True:
            if(op3 == 1):
                for i in extratoCompleto:
                    print(
                        i.tipo,
                        i.descricao,
                        i.valor,
                        i.dataOperacao)
            elif(op3 == 2):
                for i in (len(dividas)):
                    if(i.tipo == "-"):
                        print(
                            i.tipo,
                            i.descricao,
                            i.valor,
                            i.dataOperacao)
            elif(op3 == 3):
                for i in (len(lançamentos)):
                    if(i.tipo == "-"):
                        print(
                            lançamentos[i].tipo,
                            lançamentos[i].descricao,
                            lançamentos[i].valor,
                            lançamentos[i].dataOperacao)
            elif(op3 == 4):
                os.system("cls")
                break
            else:
                print("ERRO! Opção invalida ! ")
    elif op == 4:
        repetir = False
    elif op == 5:
        break
    else:
        print("Erro olhar um valor entre 1 e 4")
