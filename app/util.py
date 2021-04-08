from pathlib import Path
import io



class Arquivo:
    @staticmethod
    def criar(nome_do_arquivo):
        if not Path(nome_do_arquivo).exists():
            Path(nome_do_arquivo)


    @staticmethod
    def contar_linhas(nome_do_arquivo):
        try:
            arquivo = open(nome_do_arquivo, 'r')
            quantidade_de_linhas = len(arquivo.readlines())
            arquivo.close()

            return quantidade_de_linhas
        except FileNotFoundError:
            return 0


    @staticmethod
    def escrever(nome_do_arquivo, linha):
        '''
        >>> nome = "teste"
        >>> escrever(nome)

        '''

        quantidade_atual_de_linhas = Arquivo.contar_linhas(nome_do_arquivo)
        arquivo = open(nome_do_arquivo, 'a')
        try:
            arquivo.write(str(quantidade_atual_de_linhas) + ', ' + linha + '\n')

            return arquivo 

        except io.UnsupportedOperation:
            arquivo.write("0, " + linha + '\n')

            return arquivo 

        finally:
            arquivo.close()



    @staticmethod
    def ler(nome_do_arquivo):
        '''
        >>> nome = "teste"
        >>> escrever(nome, "teste")
        >>> ler(nome)
        teste
        '''
        arquivo = Path(nome_do_arquivo)
        return arquivo.read_text()

    
    @staticmethod
    def remover():
        return 0    

