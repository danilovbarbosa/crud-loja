from pathlib import Path

class Arquivo:
    @staticmethod
    def criar(nome_do_arquivo):
        if not Path(nome_do_arquivo).exists():
            Path(nome_do_arquivo)


    @staticmethod
    def escrever(nome_do_arquivo, linha):
        '''
        >>> nome = "teste"
        >>> escrever(nome)

        '''
        arquivo = Path(nome_do_arquivo).open('a')
        arquivo.write(linha + '\n')
        arquivo.close()
        return arquivo 

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

