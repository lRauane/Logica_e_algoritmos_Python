# Faça um Programa que
# peça as 4 notas bimestrais e mostre a média.
nota1 = int(input('primeira nota:'))
nota2 = int(input('segunda nota:'))
nota3 = int(input('terceira nota:'))
nota4 = int(input('quarta nota:'))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media > 7:
    print('Voce foi aprovado! parabens!')
else:
    print('voce foi reprovado')

print('A média entre as notas do seu semestre é: {}'.format(media))