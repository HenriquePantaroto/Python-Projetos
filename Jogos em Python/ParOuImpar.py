import random
from time import sleep
computadorNum = random.randint(1, 10)
oper = ''
print('-='*25)
print('\033[31mSeja bem vindo ao Jogo do PAR ou IMPAR!')
sleep(2)
print('\nEu, o computador, sou seu desafiante, prepare-se!\033[m')
print('-='*25)
sleep(2)
jogadorNum = int(input('\nDigite um valor de 1 à 10: '))
jogador = str(input('\nDigite qual sua opção: [Par/Impar] ')).strip().title()
soma = jogadorNum + computadorNum

while oper != 'sair':
    if jogador == 'Par':
        print()
        print('-=' * 25)
        print('\033[32mJogador: Par!\033[m')
        sleep(1.5)
        print('\n\033[32mComputador: Impar!\033[m')
        print('-=' * 25)
        sleep(1.5)
        if soma % 2 == 0:
            print(f'\nVocê ganhou, a sua escolha foi {jogadorNum} e a minha foi {computadorNum}!')
        else:
            print(f'\nEu ganhei de você, eu escolhi {computadorNum}, e você escolheu {jogadorNum}')
    if jogador == 'Impar':
        print()
        print('-=' * 25)
        print('\033[32mJogador: Impar!\033[m')
        sleep(1.5)
        print('\n\033[32mComputador: Par!\033[m')
        print('-=' * 25)
        sleep(1.5)
        if soma % 2 == 1:
            print(f'\nVocê ganhou, a sua escolha foi {jogadorNum} e a minha foi {computadorNum}!')
        else:
            print(f'\nEu ganhei de você, eu escolhi {computadorNum}, e você escolheu {jogadorNum}')
    oper = str(input('\nQuer jogar de novo? [Sim/Sair] ')).strip()
    if oper == 'sair':
        oper += oper
        break
    elif oper == 'sim':
        computadorNum = random.randint(1, 10)
        jogadorNum1 = int(input('\nDigite um valor de 1 à 10: '))
        jogadorNum = jogadorNum1
        jogador1 = str(input('\nDigite qual sua opção: [Par/Impar] ')).strip().title()
        jogador = jogador1

print('\n\033[32mFinalizando Jogo...')
sleep(1.5)
print('Jogo do PAR ou IMPAR encerrado!\033[m')
