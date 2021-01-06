lista = []
dados = []
oper = ''
maior = menor = 0
nomeMaior = ''
nomeMenor = ''

while oper != 'sair':
    dados.append(str(input('Digite o seu nome: ')))
    dados.append(int(input('Digite o seu peso: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
            nomeMaior = dados[0]
        if dados[1] < menor:
            menor = dados[1]
            nomeMenor = dados[0]
    lista.append(dados[:])
    dados.clear()
    oper = str(input('Deseja continuar? [Sim/Sair] ')).strip().lower()
    if oper == 'sair':
        break

print('-=' * 30)
print(f'Foram cadastradas {len(lista)} pessoas no total.')
print(f'O maior peso foi de {maior}Kg, da pessoa {nomeMaior}')
print(f'O menor peso foi de {menor}Kg, da pessoa {nomeMenor}')
