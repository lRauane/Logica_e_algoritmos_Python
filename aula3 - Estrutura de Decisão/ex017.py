# João Papo-de-Pescador, homem de bem, comprou um
# microcomputador para controlar o rendimento diário
# de seu trabalho. Toda vez que ele traz
# um peso de peixes maior que o estabelecido
# pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável
# peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite
# e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

quilo_peixe = int(input('Quantos quilos de peixe voce pescou?'))

if quilo_peixe > 50:
    peso_peixe = quilo_peixe - 50
    multa = 4 * peso_peixe
    print('voce pescou {}kg quilos de peixe {}kg a mais do que a regulamentção e recebeu uma multa de R${}'.format(quilo_peixe,peso_peixe, multa))
else:
    print("voce pescou {} quilos de peixe".format(quilo_peixe))
