print("🍦 Bem-vindo a sorveteria da Rauane Lima 🍦")
print("------------------------------------------------CARDÁPIO------------------------------------")
print("CÓDIGO | DESCRIÇÃO           | TAMANHO P (500ml) | Tamanho M (1000ml) | Tamanho G (2000ml) |")
print("    TR | Sabores Tradicionais|        R$  6,00   |           R$ 10,00 |           R$ 18,00 |")
print("    ES | Sabores Especiais   |        R$  7,00   |           R$ 12,00 |           R$ 21,00 |")
print("    PR | Sabores Premium     |        R$  8,00   |           R$ 14,00 |           R$ 24,00 |")
print("--------------------------------------------------------------------------------------------")

acumulador = 0  # ACUMULAR VALORES DE SORVETES

while True:
    tamanho = input("Entre com o TAMANHO do pote desejado (P/M/G): ")
    tamanho = tamanho.upper()

    codigo = input("Entre com o CÓDIGO do sabor desejado (TR| ES | PR): ")
    codigo = codigo.upper()

    if (tamanho != 'P' and tamanho != 'M' and tamanho != 'G') or (codigo != 'TR' and codigo != 'ES' and codigo != 'PR') :
        print("!!!!!!! TAMANHO ou CÓDIGO INVÁLIDO(s) !!!!!!!")
        continue

    if codigo == 'TR' and tamanho == 'P':
        print("Você pediu um sorvete sabor TRADICIONAL {} de R$ 6,00".format(tamanho))
        acumulador += 6
    elif codigo == 'TR' and tamanho == 'M':
        print("Você pediu um sorvete sabor TRADICIONAL {} de R$ 10,00".format(tamanho))
        acumulador += 10
    elif codigo == 'TR' and tamanho == 'G':
        print("Você pediu um sorvete sabor TRADICIONAL {} de R$ 18,00".format(tamanho))
        acumulador += 18

    if codigo == 'ES' and tamanho == 'P':
        print("Você pediu um sorvete sabor ESPECIAL {} de R$ 7,00".format(tamanho))
        acumulador += 7
    elif codigo == 'ES' and tamanho == 'M':
        print("Você pediu um sorvete sabor ESPECIAL {} de R$ 12,00".format(tamanho))
        acumulador += 12
    elif codigo == 'ES' and tamanho == 'G':
        print("Você pediu um sorvete sabor ESPECIAL {} de R$ 21,00".format(tamanho))
        acumulador += 21

    if codigo == 'PR' and tamanho == 'P':
        print("Você pediu um sorvete sabor PREMIUM {} de R$ 8,00".format(tamanho))
        acumulador += 8
    elif codigo == 'PR' and tamanho == 'M':
        print("Você pediu um sorvete sabor PREMIUM {} de R$ 14,00".format(tamanho))
        acumulador += 14
    elif codigo == 'PR' and tamanho == 'G':
        print("Você pediu um sorvete sabor PREMIUM {} de R$ 24,00".format(tamanho))
        acumulador += 24
    print("---------------------------------------------------------")

    maisPedidos = input("Deseja pedir mais alguma coisa? (S | N)")
    maisPedidos = maisPedidos.upper()
    if maisPedidos == 'S':
        continue
    else:
        print("O valor total a ser pago é de R${:.2f}. Volte sempre!❤".format(acumulador))
        break

