import random
from time import sleep

print('\n\033[36m-=-=-=-=-=-Seja bem vindo ao desafio JOKÊNPO-=-=-=-=-=-\033[m\n')
sleep(2)
print('\033[36mEu sou seu desafiante, quero ver você me vencer!\033[m\n')
sleep(2)
print('\033[36mO desafio é simples, basta você escrever qual das opções você irá lançar.\033[m\n')
sleep(2)
print('\033[36mLembrando que:\033[m\n')
sleep(2)
print('\033[31mPapel > Pedra\033[m')
sleep(2)
print('\033[31mPedra > Tesoura\033[m')
sleep(2)
print('\033[31mTesoura > Papel\033[m')
sleep(2)

print('\033[36mEstá pronto?\033[m\n')

lista = ['pedra', 'papel', 'tesoura']
computador = random.choice(lista)
usuario = input('Faça sua escolha (Pedra, Papel, Tesoura): ').lower()
print('Eu escolhi {}.'.format(computador))
if computador == usuario:
    print('Nós empatamos, vamos de novo.')
elif computador == 'pedra' and usuario == 'papel':
    print('Você me venceu.')
elif computador == 'pedra' and usuario == 'tesoura':
    print('Eu ganhei de você.')
elif computador == 'papel' and usuario == 'pedra':
    print('Eu ganhei de você.')
elif computador == 'papel' and usuario == 'tesoura':
    print('Você me venceu.')
elif computador == 'tesoura' and usuario == 'papel':
    print('Eu ganhei de você.')
elif computador == 'tesoura' and usuario == 'pedra':
    print('Você me venceu.')
else:
    print('Palavra não identificada, tente novamente.')

