from TesteCurso import moeda

p = float(input('Digite o valor do produto: R$'))
a = int(input('Digite a porcetagem de acrescimo: '))
d = int(input('Digite a porcetagem de desconto: '))

print(f'O dobro do valor R${p:.2f} é R${moeda.dobro(p):.2f}.')
print(f'A metade do valor R${p:.2f} é R${moeda.metade(p):.2f}.')
print(f'Aumentando {a}% do valor R${p:.2f} temos R${moeda.aumentar(p, a):.2f}.')
print(f'Diminuindo {d}% do valor R${p:.2f} temos R${moeda.diminuir(p, d):.2f}.')
