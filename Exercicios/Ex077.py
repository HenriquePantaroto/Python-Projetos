lista = ('Programar', 'Python', 'Programação', 'Computador', 'Windows', 'Apple')
vogais = 'a', 'e', 'i', 'o', 'u'
for p in lista:
    print(f'\nAs vogais de {p} são: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

print('\nFIM')
