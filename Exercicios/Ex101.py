def voto(ano):
    from datetime import date
    a = date.today().year - ano
    if a >= 18 and a < 65:
        print('-=' * 25)
        print(f'Com {a} anos, o voto é \033[32mOBRIGATÓRIO\033[m.')
        print('-=' * 25)
    elif a >= 65 or a >= 16:
        print('-=' * 25)
        print(f'Com {a} anos, o voto é \033[32mOPCIONAL\033[m.')
        print('-=' * 25)
    else:
        print('-=' * 25)
        print(f'Com {a} anos, você \033[32mnão vota\033[m.')
        print('-=' * 25)

print('-=' * 25)
ano = int(input('Digite o ano que você nasceu: '))
voto(ano)
