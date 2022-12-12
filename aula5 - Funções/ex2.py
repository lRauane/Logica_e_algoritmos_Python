def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print("Erro na criação do arquivo")
    else:
        print("arquivo {} foi criado com sucesso\n".format(nomeArquivo))

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def cadastrarJogo(nomearquivo, nomeJogo, nomeVideoGame):
    try:
        a = open(nomearquivo, 'at')
    except:
        print("Erro ao abrir o arquivo")
    else:
        a.write('{};{}\n'.format(nomeJogo, nomeVideoGame))
    finally:
        a.close()

def listarJogos(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print("erro ao ler o arquivo")
    else:
        print(a.read())
    finally:
        a.close()

# programa principal
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print("Arquivo localizado no computador")
else:
    print("Arquivo inexistente")
    criaArquivo(arquivo)

while True:
    print('MENU')
    print("1 - Cadastrar novo item")
    print("2 - Listar cadastro")
    print("3 - SAIR")

    op = valida_int("Escolha a opção desejada: ", 1, 3)
    if op == 1:
        print('Opção de cadastrar novo item selecionado!\n')
        nomeJogo = input("Nome do jogo: ")
        nomevideoGame = input("Nome do video-game: ")
        cadastrarJogo(arquivo, nomeJogo, nomevideoGame)
    elif op == 2:
        print('Opção de listar selecionado\n')
        listarJogos(arquivo)
    elif op == 3:
        print("Encerrando o programa...")
        break