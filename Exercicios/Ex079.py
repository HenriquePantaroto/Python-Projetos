valores = []
oper = ''

while oper != 'sair':
    n = int(input('Digite o valor a ser adicionado a sua Lista: '))
    if n not in valores:
        valores.append(n)
    else:
        print('Este valor é duplicado, não irei adiciona-lo.')
    oper = str(input('Deseja continuar?: [Sim/Sair] ')).lower().strip()
    if oper == 'sair':
        break


valores.sort()
print(f'A sua lista, ordenada no formato crescente, é esta: {valores}')
