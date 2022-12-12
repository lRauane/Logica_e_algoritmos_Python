# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu
# peso ideal, utilizando as seguintes fórmulas:

altura = float(input('Qual a sua altura?'))
genero = input('voce é homem ou mulher? (H - M)')

if genero == 'H':
    peso1 = (72.7 * altura) - 58
    print('voce é {} e seu peso ideal é de:{}'.format(genero, peso1))
elif genero == 'M':
    peso2 = (62.1 * altura) - 44.7
    print('voce é {} e seu peso ideal é de:{}'.format(genero, peso2))
else:
    print('valor inválido!')
