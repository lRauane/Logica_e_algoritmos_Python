preco = float(input("Digite o preço do produto:"))
p = float(input("Digite percentual do desconto (0 - 100)%: "))

desconto = preco * (p / 100)
final = preco - desconto

print('o preço do produto é: {}. Desconto de {}%'.format(preco, p))
print('valor calculado de desconto: {}. Valor final do produto: {}'.format(desconto, final))

