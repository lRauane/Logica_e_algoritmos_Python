quantidadeKm = int(input("Quantos KM voce pecorreu?"))
quantidadeDias = int(input("E quantos dias o carro foi alugado?"))

precoPagar = (60 * quantidadeDias) + (0.15 * quantidadeKm)

print('Km= {}. Dias = {}'.format(quantidadeKm, quantidadeDias))

print('O preço a pagar vai ser de:{}'.format(precoPagar))

