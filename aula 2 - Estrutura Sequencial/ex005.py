# importa funcionalidades
from datetime import datetime

odds = [1, 3, 5, 6, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 55, 57, 59]

# # criar um objeto que representa a hora de hoje,
# e então extrair o valor do atributo de minuto antes de atribuir a
# uma variável.

# time_now = datetime.today()
# Primeiro, determine a hora atual...

right_this_minute = datetime.today().minute


if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print('Not an odd minutes.')

