matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor da posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
    if matriz[1][0] > matriz[1][1] and matriz[1][0] > matriz[1][2]:
        maior = matriz[1][0]
    elif matriz[1][1] > matriz[1][0] and matriz[1][1] > matriz[1][2]:
        maior = matriz[1][1]
    else:
        maior = matriz[1][2]

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'\nA soma dos números pares é: {pares}.')
print(f'A soma dos valores da Terceira Coluna é: {soma}.')
print(f'O maior valor na linha 2 da Matriz é o {maior}.')
print(f'O maior valor na linha 2 da Matriz é o {max(matriz[1])}')
