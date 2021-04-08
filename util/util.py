from pathlib import Path

class Arquivo:
    @staticmethod
    def escrever(nome_do_arquivo, texto):
        '''
        >>> nome = "teste"
        >>> escrever(nome)

        '''
        arquivo = Path(nome_do_arquivo).open('a')
        arquivo.write(texto + '\n')
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

