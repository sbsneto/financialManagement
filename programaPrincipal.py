import os
import time
import random
from menus import cabecalho, menuLancamento, menu_principal, menu_secundario, extratos, editarExcluir
from tratarErros import leia_int, leia_str
from conta import Conta
from debitoCredito import DebitoCredito
from limpa_tela import limpa
from log import Log


contaCliente: Conta
log: Log
logs = []
extratoCompleto = []
contas = []


while True:

    limpa()
    cabecalho()
    menu_principal()
    op = leia_int('Escolha a opção desejada: ')
    limpa()

    if op == 1:

        cabecalho()
        print(" ")

        nomeCliente = leia_str("Insira o nome do Cliente: ")
        numConta = leia_int("Insira o número da conta: ")
        saldo = float(input("Insira o saldo atual da conta: R$"))

        dateTime = time.strftime(
            '%Y-%m-%d', time.localtime())

        idTransacao = random.randint(0, 9999)

        contaCliente = Conta(numConta, nomeCliente, saldo, "Cadastro Conta")
        gasto = DebitoCredito(idTransacao,
                              saldo, "+", "CADASTRO CONTA", dateTime.upper())

        extratoCompleto.append(gasto)

        idTransacao = random.randint(0, 9999)
        if(len(logs) > 6):
            logs.pop(0)
            dateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            tipo = "CADASTRO DE CONTA"
            id = idTransacao
            log = Log(dateTime, tipo, id)
            logs.append(log)
        else:
            dateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            tipo = "CADASTRO DE CONTA"
            id = idTransacao
            log = Log(dateTime, tipo, id)
            logs.append(log)

        limpa()
        print("Conta cadastrada com sucesso...")
        time.sleep(1)
        limpa()

    elif op == 2:

        while True:

            cabecalho()
            print(" ")
            menu_secundario()
            op2 = leia_int('Escolha a opção desejada: ')
            limpa()

            if (op2 == 1):

                descricao = str(input("Descrição do Debito: "))
                tipo = str("-")
                valor = float(input("Insira o valor do Debito: R$"))
                dataOp = str(input("Insira a data: "))

                idTransacao = random.randint(0, 9999)

                contaCliente.debito(valor)

                gasto = DebitoCredito(idTransacao,
                                      valor, tipo.upper(), descricao.upper(), dataOp.upper())

                extratoCompleto.append(gasto)

                if len(contas) > 1:
                    i = 0
                    while i < len(contas):
                        print(
                            contas[i].numConta,
                            contas[i].nomeCliente)
                        i += 1
                    idEditar = leia_int('Insira o ID da transação: ')
                    j = 0
                    while j < len(extratoCompleto):
                        if(extratoCompleto[j].idTransacao == idEditar):
                            extratoCompleto[j].descricao = str(
                                input("Nova descrição: "))
                            extratoCompleto[j].valor = float(
                                input("Insira o novo valor: "))
                            extratoCompleto[j].dataOperacao = str(
                                input("Insira a nova data: "))

                if(len(logs) > 6):
                    logs.pop(0)
                    dateTime = time.strftime(
                        '%Y-%m-%d %H:%M:%S', time.localtime())
                    tipo = "CADASTRO DE DÉBITO"
                    id = idTransacao
                    log = Log(dateTime, tipo, id)
                    logs.append(log)
                else:
                    dateTime = time.strftime(
                        '%Y-%m-%d %H:%M:%S', time.localtime())
                    tipo = "CADASTRO DE DÉBITO"
                    id = idTransacao
                    log = Log(dateTime, tipo, id)
                    logs.append(log)

                limpa()
                print("Débito cadastrado com sucesso...")
                time.sleep(1)
                limpa()

            elif (op2 == 2):

                descricao = str(input("Descrição do crédito: "))
                tipo = str("+")
                valor = float(input("Insira o valor do crédito: R$"))
                dataOp = str(input("Insira a data: "))

                idTransacao = random.randint(0, 9999)

                contaCliente.credito(valor)

                credito = DebitoCredito(idTransacao,
                                        valor, tipo.upper(), descricao.upper(), dataOp.upper())

                extratoCompleto.append(credito)

                if(len(logs) > 6):
                    logs.pop(0)
                    dateTime = time.strftime(
                        '%Y-%m-%d %H:%M:%S', time.localtime())
                    tipo = "CADASTRO DE DÉBITO"
                    id = idTransacao
                    log = Log(dateTime, tipo, id)
                    logs.append(log)
                else:
                    dateTime = time.strftime(
                        '%Y-%m-%d %H:%M:%S', time.localtime())
                    tipo = "CADASTRO DE DÉBITO"
                    id = idTransacao
                    log = Log(dateTime, tipo, id)
                    logs.append(log)

                limpa()
                print("Crédito cadastrado com sucesso...")
                time.sleep(1)
                limpa()

            elif (op2 == 0):
                limpa()
                break
            else:
                print("ERRO! Opção inválida ! ")
    elif op == 3:

        while True:
            cabecalho()
            print(" ")
            extratos()
            op3 = leia_int('Escolha a opção desejada: ')
            if(op3 == 1):
                limpa()
                cabecalho()
                i = 0
                while i < len(extratoCompleto):
                    print(
                        extratoCompleto[i].idTransacao,
                        extratoCompleto[i].tipo,
                        extratoCompleto[i].descricao,
                        extratoCompleto[i].valor,
                        extratoCompleto[i].dataOperacao)
                    i += 1
                # faz a execução do código parar até ser pressionada qualquer tecla
                a = input("")
                limpa()
            elif(op3 == 2):
                i = 0
                while i < len(extratoCompleto):
                    if(extratoCompleto[i].tipo == "-"):
                        print(
                            extratoCompleto[i].idTransacao,
                            extratoCompleto[i].tipo,
                            extratoCompleto[i].descricao,
                            extratoCompleto[i].valor,
                            extratoCompleto[i].dataOperacao)
                    i += 1
                # faz a execução do código parar até ser pressionada qualquer tecla
                a = input("")
                limpa()
            elif(op3 == 3):
                i = 0
                while i < len(extratoCompleto):
                    if(extratoCompleto[i].tipo == "+"):
                        print(
                            extratoCompleto[i].idTransacao,
                            extratoCompleto[i].tipo,
                            extratoCompleto[i].descricao,
                            extratoCompleto[i].valor,
                            extratoCompleto[i].dataOperacao)
                    i += 1
                # faz a execução do código parar ate ser pressionada qualquer tecla
                a = input("")
                limpa()
            elif(op3 == 0):
                limpa()
                break
            else:
                print("ERRO! Opção inválida ! ")
    elif op == 4:
        while True:
            limpa()
            cabecalho()
            print(" ")
            editarExcluir()
            op3 = leia_int('Escolha a opção desejada: ')
            if(op3 == 1):
                i = 0
                while i < len(extratoCompleto):
                    print(
                        extratoCompleto[i].idTransacao,
                        extratoCompleto[i].tipo,
                        extratoCompleto[i].descricao,
                        extratoCompleto[i].valor,
                        extratoCompleto[i].dataOperacao)
                    i += 1
                idEditar = leia_int('Insira o ID da transação: ')
                j = 0
                while j < len(extratoCompleto):
                    if(extratoCompleto[j].idTransacao == idEditar):
                        extratoCompleto[j].descricao = str(
                            input("Nova descrição: "))
                        extratoCompleto[j].valor = float(
                            input("Insira o novo valor: "))
                        extratoCompleto[j].dataOperacao = str(
                            input("Insira a nova data: "))

                        if(len(logs) > 6):
                            logs.pop(0)
                            dateTime = time.strftime(
                                '%Y-%m-%d %H:%M:%S', time.localtime())
                            tipo = "EDIÇÃO DE LANÇAMENTO"
                            id = idTransacao
                            log = Log(dateTime, tipo, id)
                            logs.append(log)
                        else:
                            dateTime = time.strftime(
                                '%Y-%m-%d %H:%M:%S', time.localtime())
                            tipo = "EDIÇÃO DE LANÇAMENTO"
                            id = extratoCompleto[j].idTransacao
                            log = Log(dateTime, tipo, id)
                            logs.append(log)

                        time.sleep(1)
                        limpa()
                    j += 1
            elif(op3 == 2):
                i = 0
                while i < len(extratoCompleto):
                    print(
                        extratoCompleto[i].idTransacao,
                        extratoCompleto[i].tipo,
                        extratoCompleto[i].descricao,
                        extratoCompleto[i].valor,
                        extratoCompleto[i].dataOperacao)
                    i += 1
                j = 0
                idExcluir = leia_int('Insira o ID da transação: ')
                while j < len(extratoCompleto):
                    if(extratoCompleto[j].idTransacao == idExcluir):

                        if(len(logs) == 6):
                            logs.pop(0)
                            dateTime = time.strftime(
                                '%Y-%m-%d %H:%M:%S', time.localtime())
                            tipo = "EXCLUSÃO DE LANÇAMENTO"
                            id = extratoCompleto[j].idTransacao
                            log = Log(dateTime, tipo, id)
                            logs.append(log)
                        else:
                            dateTime = time.strftime(
                                '%Y-%m-%d %H:%M:%S', time.localtime())
                            tipo = "EXCLUSÃO DE LANÇAMENTO"
                            id = extratoCompleto[j].idTransacao
                            log = Log(dateTime, tipo, id)
                            logs.append(log)

                        extratoCompleto.pop(i - 1)
                        limpa()
                        print("Lançamento excluido com sucesso...")
                        # faz a execução do codigo parar por alguns segundos
                        time.sleep(1)
                        limpa()
                    j += 1

                # break
            elif(op3 == 0):
                limpa()
                break
            else:
                print("ERRO! Opção inválida ! ")
    elif op == 5:
        limpa()
        cabecalho()
        print(" ")
        print("O saldo atual é de: R$", contaCliente.getSaldo())
        print("Pressione qualquer tecla para continuar. ")
        # faz a execução do codigo parar até ser pressionada qualquer tecla
        a = input("")
        limpa()
    elif op == 6:
        limpa()
        cabecalho()
        print(" ")
        i = 0
        while i < len(logs):
            print(
                logs[i].dateTime,
                logs[i].tipo,
                logs[i].id
            )
            i += 1
        a = input("")
        limpa()
    elif op == 0:
        break
    else:
        print("Erro: escolha um valor entre 1 e 4")
