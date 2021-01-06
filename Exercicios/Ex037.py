decimal = int(input('\nDigite um número a ser convertido: '))

conversao = input('\nDigite qual conversão você deseja fazer (Binario, Octal, Hexadecimal): ').lower()

if conversao == 'binario':
    print('O número {}, convertido para Binário é {}.'.format(decimal, bin(decimal)[2:]))
elif conversao == 'octal':
    print('O número {}, convertido para Octal é {}.'.format(decimal, oct(decimal)[2:]))
elif conversao == 'hexadecimal':
    print('O número {}, convertido para Octal é {}.'.format(decimal, hex(decimal)[2:]))
else:
    print('A conversão não foi reconhecida, tente novamente.')


