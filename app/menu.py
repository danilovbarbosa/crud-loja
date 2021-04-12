import sqlite3
from .models import *


class Connect(object):

    ''' A classe Connect representa o banco de dados. '''

    def __init__(self, db_name):
        try:
            # conectando...
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            # imprimindo nome do banco
            print("Banco:", db_name)
            # lendo a versão do SQLite
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            # imprimindo a versão do SQLite
            print("SQLite version: %s" % self.data)
        except sqlite3.Error:
            print("Erro ao abrir banco.")
            return False

    def commit_db(self):
        if self.conn:
            self.conn.commit()

    def close_db(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")


# def inicializar_arquivos():
#     categoria_dao = CategoriaDAO("categorias.txt")
#     produto_dao = ProdutoDAO("produto.txt")
#     return categoria_dao, produto_dao
# categoria_dao, produto_dao = inicializar_arquivos()



def exibir_menu():
    print(
        '''
        ##################
        Escolha uma das opções abaixo:
        #################
        1 - inserir categoria;
        2 - inserir produtor;
        3 - listar categoria;
        4 - listar produtor;
        0 - sair;
        '''
    )

def escolher_opcao():
    prod = ProductDB()
    cat = CategoryDB()
    opcao = str(input("Digite o valor correspondente a sua opção:  "))

    if opcao == "0":
        exit(1)

    elif opcao == "1":
        cat.inserir_categoria()

    elif opcao == "2":
        prod.inserir_produto()

    elif opcao == "3":
        cat.imprimir_lista_de_categoria()

    elif opcao == "4":
        prod.imprimir_lista_de_produto()

    else:
        print("Opção escolhida não corresponde as possibilidades indicadas.")

class CategoryDB(object):

    tb_name = 'category'

    ''' A classe CategoryDB representa um Category no banco de dados. '''

    def __init__(self):
        self.db = Connect('product_category.db')
        self.tb_name

    # create_schema
    def criar_schema(self, schema_name='sql/product_category_schema.sql'):
        print("Criando tabela %s ..." % self.tb_name)

        try:
            with open(schema_name, 'rt') as f:
                schema = f.read()
                self.db.cursor.executescript(schema)
        except sqlite3.Error:
            print("Aviso: A tabela %s já existe." % self.tb_name)
            return False

        print("Tabela %s criada com sucesso." % self.tb_name)

    ''' CREATE '''

    def inserir_categoria(self):
        cat = Category('category_id', 'product_id', 'category_name', 'description')

        cat.category_name = str(input("Digite o nome da categoria: "))
        cat.description = str(input("Digite o descrição da categoria: "))

        # categoria = Category(nome, descricao)
        # categoria_dao.inserir(categoria.__str__())
        try:
            sql = """INSERT INTO category("category_name", "description") VALUES (?, ?);"""
            self.db.cursor.execute(sql, (cat.category_name, cat.description))
            # gravando no bd
            self.db.commit_db()
            print("Dados inseridos com sucesso.")
        except sqlite3.IntegrityError:
            return False
    # read_all_customer
    def imprimir_lista_de_categoria(self):
        sql = 'SELECT * FROM category ORDER BY category_name'
        c = self.db.cursor.execute(sql)
        try:
            result = self.db.cursor.fetchall()
            for r in result:
                print(r)
        except FileNotFoundError:
            print("Não há categorias registradas.")
        return c.fetchall()


    # def imprimir_lista_de_categoria():
    #     try:
    #         print(categoria_dao.listar())
    #     except FileNotFoundError:
    #         print("Não há categorias registradas.")



class ProductDB(object):

    tb_name = 'product'

    ''' A classe CategoryDB representa um Product no banco de dados. '''

    def __init__(self):
        self.db = Connect('product_category.db')
        self.tb_name

    # create_schema
    def criar_schema(self, schema_name='sql/product_category_schema.sql'):
        print("Criando tabela %s ..." % self.tb_name)

        try:
            with open(schema_name, 'rt') as f:
                schema = f.read()
                self.db.cursor.executescript(schema)
        except sqlite3.Error:
            print("Aviso: A tabela %s já existe." % self.tb_name)
            return False

        print("Tabela %s criada com sucesso." % self.tb_name)

    ''' CREATE '''

    def inserir_produto(self):
        cat = Category('category_id', 'product_id', 'category_name', 'description')
        prod = Product('product_id', 'category_id', 'product_name', 'value', 'description','category_name')
        prod.product_name = str(input("Digite o nome da produto: "))
        prod.value = str(input("Digite a valor do produto: "))
        prod.description = str(input("Digite a descição do produto: "))
        prod.category_name = str(input("Digite o nome de uma categoria já registrada: "))
        self.db.cursor.execute(""" SELECT category_id FROM category WHERE category_name == ? ;""", (prod.category_id,))
        result = self.db.cursor.fetchall()
        for r in result:
            prod.category_id = result

        # produto = Product(nome, valor, descricao, categoria)
        # produto_dao.inserir(produto.__str__())
        try:
            sql = """ INSERT INTO product ("category_id", "product_name", "value", "description", "category_name") VALUES (?,?,?,?,?);""" 
            self.db.cursor.execute(sql, (prod.category_id, prod.product_name, prod.value, prod.description, prod.category_name))
            # gravando no bd
            self.db.commit_db()
            print("Dados inseridos com sucesso.")
        except sqlite3.IntegrityError:
            return False

    

    def imprimir_lista_de_produto(self):
        sql = 'SELECT * FROM product ORDER BY product_name'
        c = self.db.cursor.execute(sql)
        try:
            result = self.db.cursor.fetchall()
            for r in result:
                print(r)
        except FileNotFoundError:
            print("Não há Produtos registradas.")
        return c.fetchall()

    # def imprimir_lista_de_produto():
    #     try:
    #         print(produto_dao.listar())
    #     except FileNotFoundError:
    #         print("Não há produtos registrados.")