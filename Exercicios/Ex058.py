import random
computador = random.randint(1, 10)

print('Bem vindo ao jogo da adivinhação')
print('Tente adivinhar o número que estou pensando, de 1 à 10.')
print('No final te direi quantas tentativas foram necessárias para você acertar.\n')

tentativa = 0
tentativa1 = 0

while tentativa != computador:
    tentativa = int(input('Digite um número de 1 à 10: '))
    tentativa1 += 1
    if tentativa == computador:
        print('Você acertou, o número que eu pensei foi {} e o seu foi {}.'.format(computador, tentativa))

print('A quantidade de vezes, até você acertar foram {}.'.format(tentativa1))
