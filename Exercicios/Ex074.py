from random import randint

lista = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os números sorteados foram estes: {lista}')
print(f'O maior número é o {max(lista)}.')
print(f'O menor número é o {min(lista)}.')
