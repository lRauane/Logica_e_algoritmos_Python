# --------- variaveis globais -------
lista_produtos = []
codigo_produto = 0

# --------- Inicio de Cadastrar_produtos ---------
def cadastrar_produto(codigo):
    print("Bem-vindo ao menu de cadastrar produtos!!")
    print("Codigo do produto: {}".format(codigo))
    nome = input("entre com o NOME do produto: ")
    fabricante = input("entre com o FABRICANTE do produto: ")
    preco = int(input("entre com o PREÇO(R$) do produto: "))

    dicionario_produto = {
        'codigo': codigo,
        'nome': nome,
        'fabricante': fabricante,
        'preço': preco
    }

    lista_produtos.append(dicionario_produto.copy())

# --------- Inicio de Consultar_produtos ---------
def consultar_produto():
    print("Bem-vindo ao menu de consultar produtos!!")
    while True:
        opcao_consultar = input("Escolha a opção desejada:\n" +
                                    "1 - Consultar TODOS os produtos \n" +
                                    "2 - Consultar produtos por CÓDIGO \n" +
                                    "3 - Consultar produto por FABRICANTE \n" +
                                    "4 - Retornar \n" +
                                    ">> "
                                    )
        if opcao_consultar == '1':
             print("voce escolheu a opção consultar TODOS os produtos")

             for produto in lista_produtos:
                 print("-----------------------------")
                 for key, value in produto.items():
                     print("{}: {}".format(key, value))
                 print("-----------------------------")
        elif opcao_consultar == '2':
            print("voce escolheu a opção consultar produtos por CÓDIGO")
            valor_desejado = int(input("Entre com CÓDIGO desejado: "))
            for produto in lista_produtos:
                if produto['codigo'] == valor_desejado:
                        print("-----------------------------")
                        for key, value in produto.items():
                            print("{}: {}".format(key, value))
                        print("-----------------------------")
        elif opcao_consultar == '3':
            print("voce escolheu a opção consultar produto por FABRICANTE")
            valor_desejado = input("Entre com FABRICANTE desejado: ")
            for produto in lista_produtos:
                if produto['fabricante'] == valor_desejado:
                    print("-----------------------------")
                    for key, value in produto.items():
                        print("{}: {}".format(key, value))
                    print("-----------------------------")
        elif opcao_consultar == '4':
            return
        else:
            print("opção inválida, tente novamente...")
            continue

# --------- Inicio de remover_produtos ---------
def remover_produto():
    print("Bem-vindo ao menu de remover produtos!!")
    valor_desejado = int(input("Entre com o CODIGO do produto que deseja remover: "))
    for produto in lista_produtos:
        if produto['codigo'] == valor_desejado:
           lista_produtos.remove(produto)
           print("Produto removido com sucesso")

# --------- Inicio do Main---------
print("Bem-vindo a mercearia da Rauane Lima")

while True:
    opcao_menuPrincipal = input("Escolha a opção desejada:\n" +
                                "1 - cadastrar produto \n" +
                                "2 - Consultar produto \n" +
                                "3 - Remover produto \n" +
                                "4 - Sair \n" +
                                ">> "
                                )
    if opcao_menuPrincipal == '1':
        codigo_produto = codigo_produto + 1
        cadastrar_produto(codigo_produto)

    elif opcao_menuPrincipal == '2':
        consultar_produto()
    elif opcao_menuPrincipal == '3':
        remover_produto()
    elif opcao_menuPrincipal == '4':
        print("encerrando o programa")
        break
    else:
        print("opção inválida, tente novamente...")
        continue