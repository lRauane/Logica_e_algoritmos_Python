# --------- variaveis globais -------
lista_funcionarios = []
id_funcionario = 7400


def cadastrar_funcionario(id):
    print("-------------- MENU CADASTRAR FUNCIONÁRIO -------------------")
    print("Código do Funcionário: {}".format(id))
    nome = input("Por favor entre com NOME: ")
    setor = input("Por favor entre com SETOR: ")
    salario = int(input("Por favor entre com SALÁRIO (R$): "))
    print("**************************************************************")

    dicionario_funcionarios = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }

    lista_funcionarios.append(dicionario_funcionarios.copy())


def consultar_funcionarios():
    print("-------------- MENU CONSULTAR FUNCIONÁRIO ------------------")
    while True:
        opcao_consultar = input("Escolha a opção desejada:\n" +
                                "1 - Consultar TODOS os Funcionários \n" +
                                "2 - Consultar Funcionários por ID \n" +
                                "3 - Consultar Funcionários por SETOR \n" +
                                "4 - Retornar \n" +
                                ">> "
                                )
        if opcao_consultar == '1':
            for funcionario in lista_funcionarios:
                print("-----------------------------")
                for key, value in funcionario.items():
                    print("{}: {}".format(key, value))
                print("-----------------------------")
        elif opcao_consultar == '2':
            id_desejado = int(input("Digite o ID do Funcionário "))
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id_desejado:
                    print("-----------------------------")
                    for key, value in funcionario.items():
                        print("{}: {}".format(key, value))
                    print("-----------------------------")
        elif opcao_consultar == '3':
            valor_desejado = input("Digite o setor do(s) funcionário: ")
            for funcionario in lista_funcionarios:
                if funcionario['setor'] == valor_desejado:
                    print("-----------------------------")
                    for key, value in funcionario.items():
                        print("{}: {}".format(key, value))
                    print("-----------------------------")
        elif opcao_consultar == '4':
            return
        else:
            print("opção inválida, tente novamente...")
            continue


def remover_funcionario():
    print("-------------- MENU REMOVER FUNCIONÁRIO ------------------")
    valor_desejado = int(input("Digite o ID do funcionário a ser removido(a): "))
    for funcionario in lista_funcionarios:
        if funcionario['id'] == valor_desejado:
            lista_funcionarios.remove(funcionario)
            print("Funcionário removido do sistema com sucesso")


# --------- Inicio do Main---------
print("-------- Bem-vindo ao Controle de Funcionários da Rauane Lima -------")

while True:
    opcao_menuPrincipal = input("-------------- MENU PRINCIPAL ------------------\n" +
                                "Escolha a opção desejada:\n" +
                                "1 - cadastrar Funcionário \n" +
                                "2 - Consultar Funcionário(s) \n" +
                                "3 - Remover Funcionário \n" +
                                "4 - Sair \n" +
                                ">> "
                                )
    if opcao_menuPrincipal == '1':
        id_funcionario = id_funcionario + 1
        cadastrar_funcionario(id_funcionario)

    elif opcao_menuPrincipal == '2':
        consultar_funcionarios()
    elif opcao_menuPrincipal == '3':
        remover_funcionario()
    elif opcao_menuPrincipal == '4':
        print("encerrando o programa...")
        break
    else:
        print("opção inválida, tente novamente...")
        continue
