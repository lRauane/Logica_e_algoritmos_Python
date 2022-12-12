# Faça um Programa que leia
# três números e mostre-os em ordem decrescente.

n1 = int(input("Digite um número:"))
n2 = int(input("Digite um número:"))
n3 = int(input("Digite um número:"))

if n1 > n2 and n1 > n3:
    print("os valores em ordem decrescente:{} {} {}".format(n1, n2, n3))
elif n2 > n1 and n2 > n3:
    print("os valores em ordem decrescente:{} {} {}".format(n2, n3, n1))
else:
    print("os valores em ordem decrescente:{} {} {}".format(n3, n2, n1))