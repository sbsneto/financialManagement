class Conta:

    numConta: int
    nomeCliente: str
    saldo: float
    descricao: str

    def __init__(self, numConta: int, nomeCliente: str, saldo: float, descricao: str):
        self.numConta = numConta
        self.nomeCliente = nomeCliente
        self.saldo = saldo
        self.descricao = descricao

    def setNumConta(self, numConta: int):
        self.numConta = numConta

    def getNumConta(self):
        return self.numConta

    def setNomeCliente(self, nomeCliente: str):
        self.nomeCliente = nomeCliente

    def getNomeCliente(self):
        return self.nomeCliente

    def debito(self, valor: float):
        self.saldo -= valor

    def credito(self, saldo: float):
        self.saldo += saldo

    def setDescricao(self, descricao: str):
        self.descricao = descricao

    def getDescricao(self):
        return self.descricao
