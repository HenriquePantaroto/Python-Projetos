apro = []
jogador = {}
partida = gol = quantJog = 0

while True:
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    quantJog += 1
    partida = int(input(f'Quantas partidas o {jogador["nome"]} jogou: '))
    for c in range(0, partida):
        gol = int(input(f'Quantos gols o {jogador["nome"]} fez na partida {c+1}: '))
        jogador['gols'] = gol
        apro.append(jogador.copy())
    oper = str(input('Deseja adicionar mais jogadores? [Sim/Sair] ')).lower().strip()
    if oper == 'sair':
        break

print('-=' * 30)
print(apro)
for c in range(0, quantJog):
    print(f'[{c}] --> Jogador {apro[c]} --> Gols {apro[c]}')
print('-=' * 30)
