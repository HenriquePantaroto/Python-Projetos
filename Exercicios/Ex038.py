num1 = int(input('Digite o valor do primeiro número: '))
num2 = int(input('Digite o valor do segundo número: '))

if num1 > num2:
    print('O número {}, é maior do que o número {}.'.format(num1, num2))
elif num2 > num1:
    print('O número {}, é maior do que o número {}.'.format(num2, num1))
else:
    print('O número {} possui o mesmo valor numérico que o número {}.'.format(num1, num2))