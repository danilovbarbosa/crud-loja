class Category:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao


    def __str__(self):
        return self.nome + ", " + self.descricao

class Product:
    def __init__(self, id, nome, value, descricao, categoria):
        self.id = id
        self.nome = nome
        self.value = value
        self.descricao = descricao
        self.categoria = categoria

    
    def __str__(self):
        return self.nome + ", " + str(self.value) + ", " + self.descricao + ", " + self.categoria
