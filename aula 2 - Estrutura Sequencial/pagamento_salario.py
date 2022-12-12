# Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_hora = float(input('quanto voce ganha por hora?'))
numero_hora = float(input('quantas horas voce trabalha por mes?'))

total = ganho_hora * numero_hora

print('voce trabalhou por {}horas'.format(numero_hora))
print('o valor da hora trabalhada é de R${}'.format(ganho_hora))
print('O pagamento que deve ser recebido é de R${}'.format(total))