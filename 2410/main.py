import auxiliar

while(True):
    print("[1] Criar Pessoa")
    print("[2] Editar Pessoa")
    print("[3] Excluir pessoa")
    print("[0] Sair")

    try:
        opcao = int(input("OPÇÃO: "))
        match opcao:
            case 1:
                nome = input("Informe o nome: ")
                idade = input("Informe a idade: ")
                cpf = input("Informe o CPF: ")
                auxiliar.criarPessoa(nome, idade, cpf)

            case 2:
                nome = input("Informe o nome: ")
                idade = input("Informe a idade: ")
                cpf = input("Informe o CPF: ")
                id = int(input("Informe o ID: "))
                auxiliar.editarPessoa(nome, idade, cpf, id)

            case 3:
                id = int(input("Informe o ID:"))
                auxiliar.excluirPessoa(id)
                
            case 0:
                print("\nAté mais!" )
                break
            
            case _:
                print("Opção inválida.")

    except ValueError:
        print("Valor informado inválido.")
