# Faça um programa que pergunte o preço de três produtos e informe qual produto
# você deve comprar, sabendo que a decisão
# é sempre pelo mais barato.

p1 = int(input("Qual o valor do primeiro produto?"))
p2 = int(input("Qual o valor do segundo produto?"))
p3 = int(input("Qual o valor do terceiro produto?"))

if p1 < p2 and p1 < p3:
    print("Voce deve comprar o produto de valor {}".format(p1))
elif p2 < p1 and p2 < p3:
    print("voce deve compra o produto de valor: {}".format(p2))
else:
    print("voce deve comprar o produto o valor {}".format(p3))