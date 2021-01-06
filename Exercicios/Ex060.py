from math import factorial
num = int(input('Digite um número: '))
numf = factorial(num)
for c in range(num, -1):
    print('{} x'.format(c), end=' ')
print('O fatorial de {} é {}.'.format(num, numf))
