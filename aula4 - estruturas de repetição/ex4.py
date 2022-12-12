print("Calculadora:")
print("+ ADIÇÃO | - SUBTRAÇÃO | * MULTIPLICAÇÃO | / DIVISÃO")
print("pressione outra tecla para sair")

while True:
    op = input("Qual operação deseja fazer?")
    if (op == '+') or (op == '-') or (op == '*') or (op == '/'):
        valor_1 = int(input("Digite o primeiro valor:"))
        valor_2 = int(input("Digite o segundo valor:"))

    if op == '+':
        res = valor_1 + valor_2
        print('{} + {} = {}'.format(valor_1, valor_2, res))
        continue
    elif op == '-':
        res = valor_1 - valor_2
        print('{} - {} = {}'.format(valor_1, valor_2, res))
        continue
    elif op == '*':
        res = valor_1 * valor_2
        print('{} * {} = {}'.format(valor_1, valor_2, res))
        continue
    elif op == '/':
        res = valor_1 / valor_2
        print('{} / {} = {}'.format(valor_1, valor_2, res))
        continue
    elif op == 's':
        break
    else:
        print("operação invalido")


print("programa encerrando...")