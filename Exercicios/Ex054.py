menor = 0
maior = 0

for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    if ano >= 2003:
        menor += 1
    elif ano <= 2002:
        maior += 1
    else:
        print('Erro na Digitação, volte ao inicio')

print('A quantidade de pessoas menores de idade é {}.'.format(menor))
print('A quantidade de pessoas maiores de idade é {}.'.format(maior))
