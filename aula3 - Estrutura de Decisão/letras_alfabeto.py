# Faça um Programa que verifique se
# uma letra digitada é vogal ou consoante.

letras = input("Digite uma letra do alfabeto:")

if letras == 'a' or letras == 'e' or letras == 'i' or letras == 'o' or letras == 'u':
    print("A letra {} é uma vogal!".format(letras))
else:
    print("A letra {} é uma consoante!".format(letras))