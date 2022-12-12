cadastro = {'nome': [], 'sexo': [], 'ano': []}

while True:
    terminar = input("Deseja cadastrar uma pessoa?[s/n]: ")
    if terminar.upper() in 'N':
        print("Encerrando programa...")
        break
    if terminar.upper() not in 'S':
        print("Digite S para sim e N para não")
        continue

    nome = input("Qual seu nome?")
    sexo = input("Qual seu sexo?[F/M]")
    ano = int(input("Qual seu ano de nascimento?"))
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

print(cadastro)

