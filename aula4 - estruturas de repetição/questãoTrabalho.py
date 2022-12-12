print("🍕Bem-vindo a pizzaria da Rauane Lima Jesus🍕")
print("------------------------CARDÁPIO-------------------------")
print("CÓDIGO | DESCRIÇÃO | PIZZA MÉDIA (M) | PIZZA GRANDE (G) |")
print("    21 | Napolitana|        R$ 20,00 |         R$ 26,00 |")
print("    22 | Margureita|        R$ 20,00 |         R$ 26,00 |")
print("    23 | Calabresa |        R$ 25,00 |         R$ 32,50 |")
print("    24 | Toscana   |        R$ 30,00 |         R$ 39,00 |")
print("    25 | Portuguesa|        R$ 30,00 |         R$ 39,00 |")
print("---------------------------------------------------------")

acumulador = 0

while True:
    tamanho = input("Entre com o tamanho de pizza desejada (M/G): ")
    tamanho = tamanho.upper()

    if tamanho != 'M' and tamanho != 'G':
        print("Opção inválida. Digite um tamanho válido (M/G)")
        continue

    codigo = input("Entre com o código da pizza desejada (21|22|23|24|25): ")
    if codigo != '21' and codigo != '22' and codigo != '23' and codigo != '24' and codigo != '25':
        print("Opção inválida. Digite um tamanho válido (21|22|23|24|25)")
        continue

    if (codigo == '22' and tamanho == 'M') or (codigo == '21' and tamanho == 'M'):
        print("Voce escolheu a pizza Margureita tamanho G")
        acumulador += 20
    elif (codigo == '22' and tamanho == 'G') or (codigo == '21' and tamanho == 'G'):
        print("Voce escolheu a pizza Margureita tamanho G")
        acumulador += 26

    if codigo == '23' and tamanho == 'M' :
        print("Voce escolheu a pizza Calabresa tamanho M")
        acumulador += 25
    elif codigo == '23' and tamanho == 'G':
        print("Voce escolheu a pizza Calabresa tamanho G")
        acumulador += 32.50

    if (codigo == '25' and tamanho == 'M') or (codigo == '24' and tamanho == 'M'):
        print("Voce escolheu a pizza Portuguesa tamanho M")
        acumulador += 30
    elif (codigo == '25' and tamanho == 'G') or (codigo == '24' and tamanho == 'G'):
        print("Voce escolheu a pizza Portuguesa tamanho G")
        acumulador += 39

    maisPedidos = input("Deseja pedir mais alguma coisa? (S | N)")
    maisPedidos = maisPedidos.upper()
    if maisPedidos == 'S':
        continue
    else:
        print("O valor total do seu pedido é de R${:.2f}. Volte sempre!❤".format(acumulador))
        break