from models import Categoria, Produto
from util import Arquivo  


class CategoriaDAO:
    def __init__(self, nome_do_arquivo):
        self.arquivo = Arquivo.escrever(nome_do_arquivo, "")


    def inserir(self): 
        return 0


    def remover(self):
        return 0


    def listar(self):
        return 0

class ProdutoDAO:
    def __init__(self):
        pass


    def inserir(self): 
        return 0


    def remover(self):
        return 0


    def listar(self):
        return 0


if __name__ == '__main__':
    CategoriaDAO("eta")