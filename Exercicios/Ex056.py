idadeTotal = 0
homemVelho = 0
nomeHomemVelho = ''
idadeMulher = 0

for pessoas in range(1, 5):
    nome = input('Digite o nome da {}º pessoa: '.format(pessoas)).strip()
    idade = int(input('Digite a idade da {}º pessoa: '.format(pessoas)))
    sexo = input('Digite o sexo da {}º pessoa: '.format(pessoas)).lower()
    idadeTotal += idade
    if pessoas == 1 and sexo == 'masculino':
        homemVelho = idade
        nomeHomemVelho = nome
    elif idade > homemVelho and sexo == 'masculino':
        nomeHomemVelho = nome
        homemVelho = idade

    if sexo == 'feminino':
        if idade <= 20:
            idadeMulher += 1

print('\nA idade média do grupo é {}.'.format(idadeTotal / 4))
print('\nO homem mais velho do grupo é o {}, e tem {} anos.'.format(nomeHomemVelho, homemVelho))
print('\nA quantidade de mulheres com menos de 20 anos é de {}.'.format(idadeMulher))
