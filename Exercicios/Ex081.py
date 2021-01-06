oper = ''
num = []
lista = num
cont = 0

while oper != 'sair':
    num.append(int(input('Digite um número: ')))
    oper = str(input('Deseja continuar? [Sim/Sair] ')).strip().lower()
    cont += 1
    if oper == 'sair':
        break

lista.sort(reverse=True)

print(f'A quantidade de números digitados dentro da lista foram dê {cont} vezes.')
print(f'A lista em ordem Descresente é esta: {lista}')

if 5 in lista:
    print(f'O número 5 foi digitado {lista.count(5)} vezes.')
else:
    print('O número 5 não foi digitado nesta lista.')

print('FIM')
