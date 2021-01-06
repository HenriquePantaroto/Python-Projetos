from random import randint
numeros = []


def sorteia():
    for c in range(0, 5):
        sort = randint(1, 10)
        numeros.append(sort)
    print('-=' * 25)
    print(f'A lista sorteada foi esta: {numeros}.')


def somaPar():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print('-=' * 25)
    print(f'A soma dos números pares é {soma}.')
    print('-=' * 25)


sorteia()
somaPar()
