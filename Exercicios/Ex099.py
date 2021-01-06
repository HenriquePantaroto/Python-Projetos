from time import sleep


def maior(* num):
    maiorN = 0
    for n in num:
        print(f'{n} ', end='')
        sleep(0.5)
        if n > maiorN:
            maiorN = n
    print(f'\nForam informados {len(num)} números.')
    print(f'O maior número desta lista é o {maiorN}.')
    print('-=' * 25)


maior(9, 2, 1, 3, 0)
maior(3, 15, 2, 10, 2)
maior(2, 51, 35, 105, 72, 2)
maior(0)
maior()
maior(2, 1)
