total = 0
dimdim = 0

while True:
    idade = input("Qual a sua idade?")
    if idade == 'sair':
        break
    idade = int(idade)
    total += 1
    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15
    dimdim += ingresso

media = dimdim / total
print("Total de pessoas: {}".format(total))
print("Total arrecadado: {}".format(dimdim))
print("Total arrecados: {}".format(media))

