oper = ''
par = []
impar = []
lista = []

while oper != 'sair':
    num = int(input('Digite um valor: '))
    oper = str(input('Deseja continuar? [Sim/Sair] ')).lower().strip()
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    if num % 2 == 1:
        impar.append(num)
    if oper == 'sair':
        break
print('-=' * 30)
print(f'A lista contendo apenas os números pares é esta: {par}.')
print(f'A lista contendo apenas os números impares é esta: {impar}.')
print(f'A lista completa, com todos os números, é esta: {lista}.')
print('FIM')
