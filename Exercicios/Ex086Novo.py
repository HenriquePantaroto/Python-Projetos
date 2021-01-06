matriz = []

for m in range(0, 3):
    matriz.append(int(input(f'Digite o valor [0:{m}] da Matriz: ')))

for m in range(0, 3):
    matriz.append(int(input(f'Digite o valor [1:{m}] da Matriz: ')))

for m in range(0, 3):
    matriz.append(int(input(f'Digite o valor [2:{m}] da Matriz: ')))

print(f'[ {matriz[0:0]} ] [ {matriz[0:1]} ] [ {matriz[0:2]} ] ')
print(f'[ {matriz[0:3]} ] [ {matriz[0:4]} ] [ {matriz[0:5]} ] ')
print(f'[ {matriz[0:6]} ] [ {matriz[0:7]} ] [ {matriz[0:8]} ] ')
