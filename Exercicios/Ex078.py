valores = []

for cont in range(0, 5):
    valores.append(int(input(f'Digite o valor da posição {cont}: ')))
print(f'Os valores digitados foram: {valores}')
print(f'O maior valor é o {max(valores)}, e está nas posições {valores.index(max(valores))}')
print(f'O menor valor é o {min(valores)}, e está nas posições {valores.index(min(valores))}')
