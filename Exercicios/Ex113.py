def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO na digitação, tente digitar um número inteiro válido\033[m.')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário interrompeu o programa.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO na digitação, tente digitar um número inteiro válido\033[m.')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário interrompeu o programa.\033[m')
            return 0
        else:
            return n


num = leiaInt('Digite um número inteiro: ')
numReal = leiaFloat('Digite um número real: ')
print('-=' * 20)
print(f'O valor digitado foi {num}')
print(f'O valor digitado foi {numReal}')
