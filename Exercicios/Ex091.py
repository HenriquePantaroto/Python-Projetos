import random
from time import sleep
from operator import itemgetter
ranking = {}
ranking['jogador1'] = random.randint(1, 6)
ranking['jogador2'] = random.randint(1, 6)
ranking['jogador3'] = random.randint(1, 6)
ranking['jogador4'] = random.randint(1, 6)
ganhador = list()
for c, v in ranking.items():
    print(f'O {c} tirou {v} no dado.')
    sleep(1)
print('-=' * 30)
ganhador = sorted(ranking.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ganhador):
    print(f'O {i+1}º colocado foi o {v[0]}, com o valor de dado {v[1]}.')
    sleep(1)
print('-=' * 30)
print('fim')
