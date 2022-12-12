# inicio funçoes de Feijoada()
def volumeFeijoada():
    print("----------Menu 1 de 3 - Volume feijjoada ----------")
    while True:
        try:
            VolumeF = int(input("Digite a quantidade desejada (ml):"))
            if (VolumeF >= 300) and (VolumeF <= 5000):
                return VolumeF * 0.08
            else:
                print("Pare de digitar valores abaixo de 300 e acima de 5000.")
                continue
        except ValueError:
            print("Pare de digitar valores inteiros.")

def opcaoFeijoada():
    print("----------Menu 2 de 3 - Opção feijjoada ----------")
    while True:
        opcaoF = input("Qual a opção de feijoada desejada \n" +
                       'b - Básica (feijão + paiol + costelinha) \n' +
                       'p - Premium (Feijão + paiol + costelinha + partes de porco) \n' +
                       'S - (Feijão + paiol + costelinha + partes de porco + charque + bacon\n' +
                       '>> ')
        opcaoF = opcaoF.lower()
        opcaoF = opcaoF.strip()
        if opcaoF == 'b':
            return 1.00
        elif opcaoF == 'p':
            return 1.25
        elif opcaoF == 's':
            return 1.50
        else:
            print("pare de digitar opções diferentes de b/p/s")
            continue

def acompanhamentoFeijoada():
    print("----------Menu 3 de 3 - Acompanhamaneto feijoada ----------")
    acumulador = 0
    while True:
        acompanhamentoF = input("Deseja mais algum adicional: \n" +
                                '0 - Não desejo mais nada. (Encerrar pedido)\n' +
                                '1 - 200g de arroz \n' +
                                '2 - 150g de farofa especial \n' +
                                '3 - 100g de couve flor cozida \n' +
                                '4 - 1 laranja descascada \n' +
                                '>> ')
        if acompanhamentoF == '0':
            return acumulador
        elif acompanhamentoF == '1':
            acumulador += 5
            continue
        elif acompanhamentoF == '2':
            acumulador += 6
            continue
        elif acompanhamentoF == '3':
            acumulador += 7
            continue
        elif acompanhamentoF == '4':
            acumulador += 3
            continue
        else:
            print("pare de digitar opções diferentes de 0/1/2/3/4")
            continue

# inicio do main
print("----------Bem-vindo ao evento de feijoada da Rauane Lima ----------")
volume = volumeFeijoada()
opcao = opcaoFeijoada()
acompanhamento = acompanhamentoFeijoada()
total = volume * opcao + acompanhamento

print("O total ficou: R${:.2f} (Volume: R${:.2f}, Opção: R${:.2f}, Acompanhamento: R${:.2f})".format(total,volume, opcao, acompanhamento))