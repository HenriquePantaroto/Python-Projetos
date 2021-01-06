n = ''
p = 0
oper = ''

quantProdutos = p1 = valorBarato = cont = 0
barato = ''

while oper != 'sair':
    n = str(input('Digite o nome do produto: ')).lower().strip()
    p = float(input('Digite o valor do produto: R$'))
    oper = str(input('Deseja continuar? [Sim/Sair] ')).lower().strip()
    cont += 1
    p1 += p
    if p > 1000:
        quantProdutos += 1
    if cont == 1:
        valorBarato = p
        barato = n
    else:
        if p < valorBarato:
            valorBarato = p
            barato = n


print(f'O total gasto em sua compra foi R${p1:.2f}.')
print(f'A quantidade de produtos acima de R$1.000,00 foi de {quantProdutos} produtos.')
print(f'O produto mais barato, a {barato}, custa R${valorBarato:.2f}.')
print('Fim da operação: ')
