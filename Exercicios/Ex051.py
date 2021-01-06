a1 = int(input('Digite o valor do primeiro termo: '))
r = int(input('Digite o valor da razão da PA: '))
d = a1 + (10 - 1) * r
soma = 0
for c in range(a1, d + r, r):
    print('{} '.format(c),end=' ')

print('Acabou')
