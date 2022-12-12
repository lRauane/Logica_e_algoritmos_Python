# Faça um Programa que
# peça a temperatura em graus Celsius,
# transforme e mostre em graus Fahrenheit.

print('Converta Celsius para Fahrenheit:')

celsius = float(input('Qual a temperatura em Celsius?'))
f = celsius * 1.8 + 32

print('A temperatura de {} em CELSIUS é de: {}'.format(celsius, f))