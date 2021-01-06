def leiaInt():
    while True:
        print('-=' * 25)
        leiaInt = str(input('Digite um número: '))
        if leiaInt.isnumeric():
            leiaInt = int(leiaInt)
            break
        else:
            print('-=' * 25)
            print('\033[31mDigite um número inteiro válido!\033[m')
    print('-=' * 25)
    print(f'\033[32mO número digitado foi o {leiaInt}\033[m')


n = (leiaInt())
print('-=' * 25)
