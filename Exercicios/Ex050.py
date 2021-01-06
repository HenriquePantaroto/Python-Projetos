soma = 0
cont = 0
soma1 = 0
cont1 = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
    elif num % 2 == 1:
        soma1 += num
        cont1 += 1

print('A quantidade de pares é {}, e sua soma é {}.'.format(cont, soma))
print('A quantidade de impares é {}, e sua soma é {}.'.format(cont1, soma1))
