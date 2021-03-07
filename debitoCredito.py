class DebitoCredito:
    valor: float
    tipo: str
    descricao: str
    dataOperacao: str

    def __init__(self, valor: float, tipo: str, descricao: str, dataOperacao: str):
        self.valor = valor
        self.tipo = tipo
        self.descricao = descricao
        self.dataOperacao = dataOperacao
