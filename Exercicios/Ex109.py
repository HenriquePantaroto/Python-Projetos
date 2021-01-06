from TesteCurso import moeda

p = float(input('Digite o valor do produto: R$'))
a = int(input('Digite a porcetagem de acrescimo: '))
d = int(input('Digite a porcetagem de desconto: '))

print(f'O dobro do valor {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'A metade do valor {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'Aumentando {a}% do valor {moeda.moeda(p)} temos {moeda.aumentar(p, a, True)}')
print(f'Diminuindo {d}% do valor {moeda.moeda(p)} temos {moeda.diminuir(p, d, True)}')
