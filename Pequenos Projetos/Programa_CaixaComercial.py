from time import sleep

produto = float(input('Digite o valor do produto que deseja comprar: R$'))

sleep(1)
print('\n\033[31mCondições de pagamento\033[m')
print('\033[31mDinheiro/ Cheque à vista [1]\033[m')
print('\033[31mCartão à vista           [2]\033[m')
print('\033[31mCartão em 2x             [3]\033[m')
print('\033[31mCartão em 3x ou mais     [4]\033[m\n')
sleep(1)

pagamento = int(input('Digite qual das operações de pagamento você gostaria de efetuar: '))

if pagamento == 1:
    total = produto - (produto * (10 / 100))
elif pagamento == 2:
    total = produto - (produto * (5 / 100))
elif pagamento == 3:
    total = produto
elif pagamento == 4:
    total = produto + (produto * (20 / 100))
    parcela = int(input('Em quantas vezes você gostaria de dividir? '))
    parcelaTotal = total / parcela
    print('A parcela será de {:.2f}.'.format(parcelaTotal))

else:
    total = 9999.99
    print('A opção escolhida não existe. Tente novamente.')

print('O valor do produto é R${:.2f}, e com a forma de pagamento escolhida '
          'o valor será R${:.2f}.'.format(produto, total))
