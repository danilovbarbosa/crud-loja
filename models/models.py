class Categoria:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

class Produto:
    def __init__(self, nome, valor, descricao, categoria):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria