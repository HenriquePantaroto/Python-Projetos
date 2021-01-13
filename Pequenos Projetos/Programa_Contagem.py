from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 20)
    print('Contagem de 1 até 10, de 1 em 1.')
    for contA in range(1, 11):
        print(f'{contA} ', end='')
        sleep(0.3)
    print('Fim')
    print('-=' * 20)
    print('Contagem de 10 até 0, de 2 em 2.')
    for contB in range(10, -1, -2):
        print(f'{contB} ', end='')
        sleep(0.3)
    print('Fim')
    print('-=' * 20)


def cont(a, b, c):
    print('Agora é a sua vez de personalizar a contagem')
    a1 = int(input('Inicio: '))
    b2 = int(input('Fim: '))
    c3 = int(input('Passos: '))
    print(f'Contagem de {a1} até {b2}, de {c3} em {c3}.')
    if c3 == 0:
        c3 = 1
    for contC in range(a1, b2-1, c3):
        print(f'{contC} ', end='')
        sleep(0.3)
    print('Fim')
    print('-=' * 20)


contador('inicio', 'fim', 'passo')
cont('a', 'b', 'c')



