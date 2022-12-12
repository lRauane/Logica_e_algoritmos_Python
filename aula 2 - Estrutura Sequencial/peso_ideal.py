# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
# que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Qual a sua altura?'))
peso_ideal = (72.7 * altura) - 58

print('voce tem {} de altura e seu peso ideal é de:{}'.format(altura, peso_ideal))