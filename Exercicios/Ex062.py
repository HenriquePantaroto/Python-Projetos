primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        cont += 1
        termo += razao
        print('{} -> '.format(termo), end=' ')
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer ver: '))

print('Fim do Programa!')
