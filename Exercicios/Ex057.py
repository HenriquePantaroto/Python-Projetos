sexo = str(input('Digite o seu sexo [M/F]: ')).upper()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informação errada, digite novamente o seu sexo [M/F]: ')).upper()

print('O seu sexo é o {}.'.format(sexo))
