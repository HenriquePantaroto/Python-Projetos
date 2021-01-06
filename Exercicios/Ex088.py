import random
from time import sleep
print('-= ' * 5, end='')
print('\033[31mSeja bem vindo ao Gerador de Números da Mega Sena !!\033[m', end='')
print(' =-' * 5)
sleep(1)
quant = int(input('\nQuantos jogos você quer que eu sorteie: '))
jogosLista = []
jogos = 0

for j in range(0, quant):
    jogos = (random.randint(1, 60), random.randint(1, 60), random.randint(1, 60),
             random.randint(1, 60), random.randint(1, 60), random.randint(1, 60))
    jogosLista.append(jogos)
    print(f'\n\033[35mJogo {j+1}:\033[m {jogos}')
    sleep(1)

print('\n\033[32mFim do Sorteio de Números, boa sorte!\033[m')
