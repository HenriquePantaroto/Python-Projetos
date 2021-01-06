from datetime import datetime
lista = {}
lista['nome'] = str(input('Digite o seu nome: '))
ano = int(input('Digite o ano de Nascimento: '))
idade = datetime.now().year - ano
lista['idade'] = idade

while True:
    cart = int(input('Número da Carteira de Trabalho: [Ou 0 para sair} '))
    lista['carteira'] = cart
    if cart == 0:
        break
    else:
        lista['contratação'] = int(input('Qual foi o ano de Contratação: '))
        lista['salário'] = float(input('Digite o valor do salário: R$'))
        apos = (lista['contratação'] - ano) + 35
        lista['aposentadoria'] = apos
        break

print('-=' * 30)
for c, v in lista.items():
    print(f'    --> {c} tem o valor {v}.')
