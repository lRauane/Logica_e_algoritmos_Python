palavras = ('Mario', 'Luigi', 'Pithi', 'yosh', 'Browser')

for palavras in palavras:
    print('\nPalavra: {}. vogais: '.format(palavras.upper(), end=''))
    for letra in palavras:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
