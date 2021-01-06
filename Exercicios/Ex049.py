num = int(input('Digite um número que queira saber a tabuada: '))
for c in range(0, 11):
    r = num * c
    print('{} x {:.0f} = {}'.format(num, c, r))

print('Fim da Tabuada.')
