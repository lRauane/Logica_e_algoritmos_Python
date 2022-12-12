print("Bem vindo a loja da Rauane Lima Jesus")
valorProduto = float(input("Entre com o valor do produto:"))
qtdProduto = int(input("Entre com a quantidade:"))
sub_total = valorProduto * qtdProduto

if sub_total < 200:
  _valorFinal = sub_total
elif 200 <= sub_total < 400:
  _valorFinal = sub_total - sub_total * 0.04
elif 400 <= sub_total < 700:
  _valorFinal = sub_total - sub_total * 0.07
else:
  _valorFinal = sub_total - sub_total * 0.10

print("o valor sem desconto: R${:.2f}".format(sub_total))
print("o valor com desconto: R${:.2f}".format(_valorFinal))