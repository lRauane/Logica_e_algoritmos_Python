kmH = float(input("Quantos kWh?"))
tipo = input("Qual o tipo de instalão (R, C ou I:)")

if tipo == 'R':
    if kmH <= 500:
      preco = 0.4
    else:
      preco = 0.65
elif tipo == 'C':
    if kmH <= 1000:
      preco = 0.55
    else:
      preco = 0.6
elif tipo == 'I':
    if kmH <= 5000:
      preco = 0.55
    else:
      preco = 0.6
else:
    print("operação inválida")

print("Total a pagar: {}".format(kmH * preco))
