from TesteCurso import moeda, dados

p = dados.leiaDinheiro('Digite um valor R$')
a = int(input('Digite o valor do aumento, em porcentagem: '))
d = int(input('Digite o valor do desconto, em porcentagem: '))
moeda.resumo(p, a, d)
