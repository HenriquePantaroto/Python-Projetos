def ficha(n, g=0):
    if nome == '':
        n = '<desconhecido>'
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = str(input('Digite o nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(nome, gols)
