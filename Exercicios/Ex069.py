idadeTotal = homem = mulher = mulherMenos = 0
resp = ''
while resp != 'sair':
    sexo = str(input('Digite o seu sexo: [M/F] ')).lower().strip()
    if sexo == 'm':
        homem += 1
    elif sexo == 'f':
        mulher += 1
    idade = int(input('Digite a sua idade: '))
    if idade > 18:
        idadeTotal += 1
    if sexo == 'f':
        mulherMenos += 1
    resp = str(input('Você deseja continuar? [Sim/Sair] ')).strip().lower()

print(f'A quantidade de pessoas com mais de 18 anos é de {idadeTotal}.')
print(f'A quantidade de homens cadastrados foi de {homem}.')
print(f'A quantidade de mulheres com menos de 20 anos é de {mulherMenos}.')
