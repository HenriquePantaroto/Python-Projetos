lista = []
dicio = {}
idadeTot = 0
cont = 0
contMulher = 0
while True:
    dicio['nome'] = str(input('Digite o nome: '))
    while True:
        dicio['sexo'] = str(input('Digite o sexo: [M/F] ')).upper()[0]
        if dicio['sexo'] in 'MF':
            break
        else:
            dicio['sexo'] = str(input('Digite apenas M ou F: ')).upper()[0]
    dicio['idade'] = int(input('Digite a idade: '))
    if dicio['sexo'] == 'F':
        contMulher += 1
    cont += 1
    idadeTot += dicio['idade']
    lista.append(dicio.copy())
    oper = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if oper not in 'SN':
        oper = str(input('Apenas S ou N, deseja continuar? ')).upper()[0]
    if oper == 'N':
        break


mediaIdade = idadeTot / cont

print('-=' * 30)
print(f'O grupo tem um total de {cont} pessoas.')
print(f'A média de idade do grupo é de {mediaIdade:.2f} anos.')
print(f'A quantidade de mulheres no grupo é de {contMulher}.')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'Nome: {p["nome"]},   Idade: {p["idade"]}.')
print('A lista de pessoas que estão acima da média são: ')
for p in lista:
    if p['idade'] > mediaIdade:
        print(f'Nome: {p["nome"]},   Sexo: {p["sexo"]},   Idade: {p["idade"]}.')
print('-=' * 30)
