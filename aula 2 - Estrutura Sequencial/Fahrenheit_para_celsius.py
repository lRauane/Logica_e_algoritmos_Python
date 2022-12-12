# Faça um Programa que peça a temperatura
# em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.

print('Converta Fahrenheit para celsius:')

Faherein = float(input('Qual a temperatura em Fahrenheit?'))
c = 5 * ((Faherein - 32) / 9)

print('A temperatura de {} em CELSIUS é de: {}'.format(Faherein, c))
