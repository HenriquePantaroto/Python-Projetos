times = ('Internacional', 'Atlético-MG', 'Flamengo', 'São Paulo', 'Fluminense', 'Palmeiras', 'Santos',
         'Grêmio', 'Bahia', 'Sport Recife', 'Corinthians', 'Fortaleza', 'Ceará', 'Atlético-GO', 'Coritiba',
         'Bragantino', 'Botafogo', 'Vasco da Gama', 'Atlético-PR', 'Goiás')
print('-='*45)
print('Os cinco primeiros colocados são: ')
print(times[0:5])
print('-='*45)
print('Os últimos quatro colocados são: ')
print(times[-4:])
print('-='*45)
print('Os times em ordem alfabética:')
print(sorted(times))
print('-='*45)
print(f'A posição do Bahia no campeonato é a {times.index("Bahia")+1}º')
print('-='*45)

print('\nFIM')

