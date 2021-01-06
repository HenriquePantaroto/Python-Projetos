from time import sleep
n = int(input('Digite um número para saber sua tabuada: '))
while n >= 1:
    for c in range(1, 11):
        r = n * c
        print(f'{n} x {c} == {r}')
    n = int(input('Digite um número positivo para saber sua tabuada, ou um número negativo para sair: '))
    if n < -1:
        break

print('\nFinalizando programa ...')
sleep(2)
print('\nFim do programa.')
