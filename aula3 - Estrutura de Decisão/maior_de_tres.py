# Faça um Programa que leia três números e mostre o maior deles

n1 = int(input("Digite um valor:"))
n2 = int(input("Digite outro número:"))
n3 = int(input("Digite outro número:"))

if n1 > n2 and n3:
    print("O maior número entre {} {} {} é: {}".format(n1, n2, n3, n1))
elif n2 > n1 and n3 :
    print("O maior número entre {} {} {} é: {}".format(n1, n2, n3, n2))
elif n3 > n2 and n1 :
    print("O maior número entre {} {} {} é: {}".format(n1, n2, n3, n3))