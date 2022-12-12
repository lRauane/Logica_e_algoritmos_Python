print("Bem-vindo a loja da Rauane Lima Jesus")
VALOR_PRODUTO = float(input("Entre com o valor do produto:"))
QUANTIDADE_PRODUTO = int(input("Entre com a quantidade:"))
VALOR_COMPRA_SUB_TOTAL = VALOR_PRODUTO * QUANTIDADE_PRODUTO

if QUANTIDADE_PRODUTO < 11:
    VALOR_FRETE = 30
elif 11 <= QUANTIDADE_PRODUTO < 101:
    VALOR_FRETE = 60
elif 101 <= QUANTIDADE_PRODUTO < 1001:
    VALOR_FRETE = 120
else:
    VALOR_FRETE = 240

print("O valor sem frete foi: R${:.2f}".format(VALOR_COMPRA_SUB_TOTAL))
print("O valor com frete foi: R${:.2f}".format(VALOR_FRETE + VALOR_COMPRA_SUB_TOTAL))
print("Frete de R${}".format(VALOR_FRETE))