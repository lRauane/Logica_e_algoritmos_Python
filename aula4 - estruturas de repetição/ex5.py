valor = int(input("Digite o valor em R$:"))

while True:
    if valor >= 100:
        cedulas_100 = valor // 100
        valor -= cedulas_100 * 100
        print("Cédulas de 100:{}".format(cedulas_100))
        if not valor:
            break
    if valor >= 50:
        cedulas_50 = valor // 50
        valor -= cedulas_50 * 50
        print("Cédulas de 50:{}".format(cedulas_50))
        if not valor:
            break
    if valor >= 20:
        cedulas_20 = valor // 20
        valor -= cedulas_20 * 20
        print("Cédulas de 20:{}".format(cedulas_20))
        if not valor:
            break
    if valor >= 10:
        cedulas_10 = valor // 10
        valor -= cedulas_10 * 10
        print("Cédulas de 10:{}".format(cedulas_10))
        if not valor:
            break
    if valor >= 5:
        cedulas_5 = valor // 5
        valor -= cedulas_5 * 5
        print("Cédulas de 5:{}".format(cedulas_5))
        if not valor:
            break
    if valor:
        cedulas_1 = valor
        print("Cédulas de 1:{}".format(cedulas_1))
        break

