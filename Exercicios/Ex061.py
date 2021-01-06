primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    cont += 1
    termo += razao
    print('{} -> '.format(termo), end=' ')

print('FIM')
