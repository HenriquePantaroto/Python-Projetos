num = 0
num1 = 0
numQuant = 0
resp = ''
numMaior = 0
numMenor = 0

while resp != 'nao':
    num = int(input('Digite o valor do número: '))
    num1 += num
    numQuant += 1
    if numQuant == 1:
        numMenor = numMaior = num
    else:
        if num > numMaior:
            numMaior = num
        elif num < numMenor:
            numMenor = num
    resp = str(input('Deseja continuar [sim/nao]: '))


print('''\nOpções de Operações
[1] Média de Valores
[2] Maior número
[3] Menor número
[4] Sair do Programa\n''')

oper = 0


while oper != 4:
    oper = int(input('Digite o valor da operação que deseja: '))
    if oper == 1:
        print('O valor da média entre os números digitados é de: {:.2f}.'.format(num1 / numQuant))
    elif oper == 2:
        print('O maior valor digitado é o {}.'.format(numMaior))
    elif oper == 3:
        print('O menor valor digitado foi o {}.'.format(numMenor))


print('\nFim do Programa')
