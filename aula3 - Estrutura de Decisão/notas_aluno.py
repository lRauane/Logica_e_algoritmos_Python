# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:

nota1 = int(input("Digite a nota do primeiro semestre:"))
nota2 = int(input("Digite a nota do segundo semestre:"))
result = (nota1 + nota2) / 2

if result >= 7:
    print("Aprovado com a média de:{}".format(result))
elif result < 7:
    print("Reprovado com a média de:{}".format(result))
else:
    print("Aprovado com Distinção e média de {]".format(result))
