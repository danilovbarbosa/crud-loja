class Categoria:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao


    def __str__(self):
        return self.nome + ", " + self.descricao

class Produto:
    def __init__(self, nome, valor, descricao, categoria):
        self.nome = nome
        self.valor = valor
        self.descricao = descricao
        self.categoria = categoria

    
    def __str__(self):
        return self.nome + ", " + str(self.valor) + ", " + self.descricao + ", " + self.categoria
