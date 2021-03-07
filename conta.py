class Conta:

    numConta: int(13216549879)
    nomeCliente: str("Sebastião Neto")
    saldo: float
    descricao: str

    def __init__(self, numConta, nomeCliente, saldo, descricao):
        self.numConta = numConta
        self.nomeCliente = nomeCliente
        self.saldo = saldo
        self.descricao = descricao

    def setNumConta(self, numConta):
        self.numConta = numConta

    def getNumConta(self):
        return self.numConta

    def setNomeCliente(self, nomeCliente):
        self.numConta = nomeCliente

    def getNomeCliente(self):
        return self.nomeCliente

    def setSaldo(self, saldo):
        self.numConta = saldo

    def getSaldo(self):
        return self.saldo

    def setDescricao(self, descricao):
        self.descricao = descricao

    def getDescricao(self):
        return self.descricao
