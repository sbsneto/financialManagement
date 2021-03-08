# Classe principal e construtor, para a abertura de contas
class Cofre:
    def __init__(self, saldo, historico, dataHistorico):
        self.saldo = saldo
        self.historico = historico
        self.dataHistorico = dataHistorico
        historico = []
        dataHistorico = []
    def getSaldo(self, saldo):
        
    
class Operacao:
    def debitaSaldo(self, valor, saldo, historico, data, dataHistorico):
        # aqui se subtrai o valor do saldo e
        # se registra a operação à pilha do histórico
        historico.append(valor)
        dataHistorico.append(data)
        saldo -= valor
    def creditaSaldo(self, valor, saldo, historico, data, dataHistorico):
        # O mesmo, agora somando
        historico.append(valor)
        dataHistorico.append(data)
        saldo += valor

class Correcao:
    def corrigeEntrada(self, historico, dataHistorico):
        # Método para apagar a última operação do histórico
        dataHistorico.pop()
        historico.pop()

