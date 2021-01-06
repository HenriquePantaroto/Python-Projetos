
############################################## PRIMEIRA SOLUÇÃO ########################################
pares = []
impares = []
lista = []

for n in range(0, 7):
    dados = int(input(f'Digite o {n}º valor: '))
    if dados % 2 == 0:
        pares.append(dados)
    elif dados % 2 == 1:
        impares.append(dados)
lista.append(pares[:])
lista.append(impares[:])

lista[0].sort()
lista[1].sort()

print('-=' * 30)
print(f'Os valores pares digitados foram: {lista[0]}.')
print(f'Os valores impares digitados foram: {lista[1]}.')

############################################## SEGUNDA SOLUÇÃO #############################################

num = [[], []]
valor = 0
for n in range(1, 8):
    valor = int(input(f'Digite o {n}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    elif valor % 2 == 1:
        num[1].append(valor)

print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'A lista completa é esta: {num}')
print(f'Os números pares digitados são: {num[0]}')
print(f'Os números impares digitados são: {num[1]}')
