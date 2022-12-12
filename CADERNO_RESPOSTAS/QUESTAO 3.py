# menu 1 de 3
def metragem_limpeza():
    print("--------------------- Menu 1 de 3 -Metragem de limpeza ----------------------")
    while True:
        try:
            metragem = int(input("Digite a metragem desejada (m²)):"))
            if (metragem >= 30) and (metragem <= 300):
                print("É necessário contratar um(uma) funcionário(a) para a limpeza\n" +
                      "*****************************************************************************")
                return 60 + 0.3 * metragem
            elif (metragem >= 300) and (metragem <= 700):
                print("Serão necessários(as) dois(duas) funcionários(as) para a limpeza\n" +
                      "*****************************************************************************")
                return 120 + 0.5 * metragem
            else:
                print("!! Não aceitamos casas com metragem menor que 30m²) ou maior que 700m²) !!")
                continue
        except ValueError:
            print("!!!!! VALOR INVÁLIDO !!!!!")


# menu 2 de 3
def tipo_limpeza():
    print("--------------------- Menu 2 de 3 - Tipo de limpeza --------------------------")
    while True:
        opcaoL = input("Entre com o tipo de limpeza desejada:\n" +
                       'B - Básica - Indicada para sujeiras semanais ou quizenais\n' +
                       'C - Completa (30% a mais) - Indicada para sujeiras antigase/ou não rotineiras\n' +
                       '>> ')

        opcaoL = opcaoL.lower()
        opcaoL = opcaoL.strip()
        if opcaoL == 'b':
            print("Voce selecionou a limpeza BÁSICA\n" +
                  "*****************************************************************************")
            return 1.00
        elif opcaoL == 'c':
            print("Voce selecionou a limpeza COMPLETA \n" +
                  "******************************************************************************")
            return 1.30
        else:
            print("!!!!! OPÇÃO INVÁLIDA !!!!!")
            continue


# menu 3 de 3
def adicional_limpeza():
    print("--------------------- Menu 3 de 3 - Adicionais de limpeza ----------------------")
    acumulador = 0
    while True:
        addLimpeza = input("Deseja mais algum adicional? \n" +
                           '0- Não desejo mais nada (encerrar) \n' +
                           '1 - Passar 10 peças de roupas - R$ 10.00 \n' +
                           '2 - Limpeza de 1 Forno/Micro-ondas - R$ 12,00 \n' +
                           '3 - Limpeza de 1 Geladeira/Freezer - R$ 20,00 \n' +
                           '>> ')
        if addLimpeza == '0':
            return acumulador
        elif addLimpeza == '1':
            acumulador += 10
            continue
        elif addLimpeza == '2':
            acumulador += 12
            continue
        elif addLimpeza == '3':
            acumulador += 20
            continue
        else:
            print("!!!!! OPÇÃO INVÁLIDA !!!!!")
            continue


# main
print("🧹🧺 Bem-vindo ao programa de Serviçoes de limpeza da Rauane Lima Jesus 🧺🧹")
metragem = metragem_limpeza()
tipos = tipo_limpeza()
adicional = adicional_limpeza()
total = (metragem * tipos) + adicional

print("TOTAL: R${:.2f} (metragem: R${:.2f} * tipo: R${:.2f} + adiocional: R${:.2f}. VOLTE SEMPRE!❤)".format(total, metragem, tipos, adicional))
