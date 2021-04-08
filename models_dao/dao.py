from models import Categoria, Produto
from util import Arquivo  


class CategoriaDAO:
    def __init__(self, nome_do_arquivo):
        self.nome_do_arquivo = nome_do_arquivo
        Arquivo.criar(nome_do_arquivo)


    def inserir(self, categoria): 
        Arquivo.escrever(self.nome_do_arquivo, categoria)


    def remover(self):
        return 0


    def listar(self):
        categorias = Arquivo.ler(self.nome_do_arquivo).splitlines()
        # categorias = [c for c in list(categorias.split() if "\n" in x]


        return categorias

class ProdutoDAO:
    def __init__(self, nome_do_arquivo):
        self.nome_do_arquivo = nome_do_arquivo
        Arquivo.criar(nome_do_arquivo)


    def inserir(self, produto): 
        Arquivo.escrever(self.nome_do_arquivo, produto)


    def remover(self):
        return 0


    def listar(self):
        produtos = Arquivo.ler(self.nome_do_arquivo).splitlines()

        return produtos


