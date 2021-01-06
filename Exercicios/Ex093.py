gol = []
apro = {}
apro['nome'] = str(input('Qual o nome do Jogador: '))
partidas = int(input(f'Digite a quantidade de Partidas que {apro["nome"]} jogou: '))
totalGols = 0
for p in range(0, partidas):
    golTot = int(input(f'Quantos gols na partida {p+1}: '))
    totalGols += golTot
    gol.append(golTot)
    apro['gols'] = gol

print('-=' * 30)
print(f'O jogador {apro["nome"]} jogou {partidas} partidas.')
for p in range(0, partidas):
    print(f'    --> Na partida {p+1} o jogador {apro["nome"]} fez {apro["gols"][p]} gols.')
print(f'O total de gols feitos pelo {apro["nome"]} no campeonato foi de {totalGols} gols.')
print('FIM')
