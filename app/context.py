# connect_db.py
# import os
import sqlite3

# conectando...
conn = sqlite3.connect('product_category.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
sql = """
CREATE TABLE IF NOT EXISTS product (
	product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	category_id INTEGER NOT NULL,
    product_name TEXT NOT NULL,
    category_name TEXT NOT NULL,
	description	VARCHAR(200) NOT NULL,
    value REAL,
    FOREIGN KEY (category_id) REFERENCES category(category_id)
);
"""
cursor.execute(sql)

# sql = """ CREATE TABLE IF NOT EXISTS Product_Category(
#     product_category_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, category_id int NOT NULL, product_id int NOT NULL);"""
# cursor.execute(sql)

print('Tabela criada com sucesso.')

sql ="""
CREATE TABLE IF NOT EXISTS category (
	category_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    category_name TEXT NOT NULL,
	description	VARCHAR(200) NOT NULL
    );"""
cursor.execute(sql)

print('Tabela criada com sucesso.')
# desconectando...
conn.close()


# class Connect(object):

#     ''' A classe Connect representa o banco de dados. '''

#     def __init__(self, db_name):
#         try:
#             # conectando...
#             self.conn = sqlite3.connect(db_name)
#             self.cursor = self.conn.cursor()
#             # imprimindo nome do banco
#             print("Banco:", db_name)
#             # lendo a versão do SQLite
#             self.cursor.execute('SELECT SQLITE_VERSION()')
#             self.data = self.cursor.fetchone()
#             # imprimindo a versão do SQLite
#             print("SQLite version: %s" % self.data)
#         except sqlite3.Error:
#             print("Erro ao abrir banco.")
#             return False

#     def close_db(self):
#         if self.conn:
#             self.conn.close()
#             print("Conexão fechada.")

# if __name__ == '__main__':
#     product = Product('product_name', 'value', 'description', 'category_name')
#     category = Category('category_name', 'description')
#     conn.close()

# db = Connect('product.db')
# db.close_db()
# dir(Connect)
# db.__dict__