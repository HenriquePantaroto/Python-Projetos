n = 0
n1 = 0
q = 0
while n != 999:
    n = int(input('Digite um número: '))
    n1 += n
    q += 1

print('A soma entre os números digitados é {}.'.format(n1 - 999))
print('A quantidade de números digitados foi de {}.'.format(q - 1))
print('FIM')
