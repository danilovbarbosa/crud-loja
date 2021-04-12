from .models import *
from .context import *




class CategoriaDAO:
    def __init__(self, nome_do_arquivo):
        self.nome_do_arquivo = nome_do_arquivo
        Arquivo.criar(nome_do_arquivo)


    def inserir(self, categoria: Category): 
        Arquivo.escrever(self.nome_do_arquivo, categoria)


    def remover(self):
        '''
        TODO: implementar
        '''
        return 0


    def listar(self):
        categorias = Arquivo.ler(self.nome_do_arquivo).splitlines()
        return categorias


    @staticmethod
    def procurar_por_nome(nome_do_arquivo, nome):
        '''
        @return: irá retornar o id da categoria
        '''
        lista_de_categorias = Arquivo.ler(nome_do_arquivo).splitlines()
        for categoria in lista_de_categorias:
            if nome in categoria:
                return categoria[0]



    ''' A classe ProductDb representa um produto no banco de dados. '''

    

   


class ProdutoDAO(object):
    def __init__(self):
        self.db = Connect('product_category.db')


    def inserir(self, produto: Product):
        Arquivo.escrever(self.nome_do_arquivo, produto)


    def remover(self):
        '''
        TODO: implementar
        '''
        return 0


    def listar(self):
        produtos = Arquivo.ler(self.nome_do_arquivo).splitlines()

        return produtos

    def close_connection(self):
        self.db.close_db()
