class DebitoCredito:
    idTransacao: int
    valor: float
    tipo: str
    descricao: str
    dataOperacao: str

    def __init__(self, idTransacao: int, valor: float, tipo: str, descricao: str, dataOperacao: str):
        self.idTransacao = idTransacao
        self.valor = valor
        self.tipo = tipo
        self.descricao = descricao
        self.dataOperacao = dataOperacao
