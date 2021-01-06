from TesteCurso import moeda

p = float(input('Digite o valor do produto: R$'))
a = int(input('Digite a porcetagem de acrescimo: '))
d = int(input('Digite a porcetagem de desconto: '))

print(f'O dobro do valor {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'A metade do valor {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'Aumentando {a}% do valor {moeda.moeda(p)} temos {moeda.moeda(moeda.aumentar(p, a))}')
print(f'Diminuindo {d}% do valor {moeda.moeda(p)} temos {moeda.moeda(moeda.diminuir(p, d))}')
