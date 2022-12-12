# Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input("Digite um valor:"))
n2 = int(input("Digite outro número:"))

if n1 > n2:
    print("O maior número entre {} e {} é: {}".format(n1, n2, n1))
elif n1 < n2:
    print("O maior número entre {} e {} é: {}".format(n1, n2, n2))