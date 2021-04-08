from .models import *
from .dao import *


categoria_dao, produto_dao = inicializar_arquivos()


def inicializar_arquivos():
    categoria_dao = CategoriaDAO("categorias.txt")
    produto_dao = ProdutoDAO("produto.txt")
    return categoria_dao, produto_dao


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
    opcao = str(input("Digite o valor correspondente a sua opção:  "))

    if opcao == "0":
        exit(1)

    elif opcao == "1":
        inserir_categoria()

    elif opcao == "2":
        inserir_produto()

    elif opcao == "3":
        print(categoria_dao.listar())

    elif opcao == "4":
        print(produto_dao.listar())
    else:
        print("Opção escolhida não corresponde as possibilidades indicadas.")


def inserir_categoria():
    nome = str(input("Digite o nome da categoria: "))
    descricao = str(input("Digite o descrição da categoria: "))

    categoria = Categoria(nome, descricao)
    categoria_dao.inserir(categoria.__str__())


def inserir_produto():
    nome = str(input("Digite o nome da categoria: "))
    valor = str(input("Digite a valor do produto: "))
    descricao = str(input("Digite a descição do produto: "))
    categoria = str(input("Digite o nome de uma categoria já registrada: "))

    produto = Produto(nome, valor, descricao, categoria)
    produto_dao.inserir(categoria.__str__())