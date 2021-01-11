from time import sleep
num1 = float(input('\nDigite o valor do primeiro número: '))
num2 = float(input('\nDigite o valor do segundo número: '))

sleep(1)

print('\n\033[32mAs Operações a seguir são as opções que você poderá escolher:\033[m\n')

sleep(1)

print('''\033[31m[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do Programa\033[m''')

sleep(1)

op = 0
soma = 0
multiplicar = 0
maior = 0

while op != 5:
    op = int(input('\n\033[32mDigite o número da operação que deseja realizar:\033[m '))
    if op == 1:
       soma = num1 + num2
       print('\nA soma entre os números {} e {}, é de {}.'.format(num1, num2, soma))
    elif op == 2:
        multiplicar = num1 * num2
        print('\nA multiplicação entre os números {} e {}, é de {}.'.format(num1, num2, multiplicar))
    elif op == 3:
        if num1 > num2:
            maior = num1
            print('\nO maior número entre {} e {}, é o {}.'.format(num1, num2, maior))
        elif num2 > num1:
            maior = num2
            print('\nO maior número entre {} e {}, é o {}.'.format(num1, num2, maior))
    elif op == 4:
        n1 = int(input('Digite o novo valor do primeiro número: '))
        n2 = int(input('Digite o novo valor do segundo número: '))
        num1 = n1
        num2 = n2

sleep(1)
print('\n\033[35mFinalizando...\033[m')
sleep(2)
print('\n\033[35mFim do Programa.\033[m')
