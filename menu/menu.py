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
        pass
    elif opcao == "2":
        pass
    elif opcao == "3":
        pass
    elif opcao == "4":
        pass
    else:
        print("Opção escolhida não corresponde as possibilidades indicadas.")
