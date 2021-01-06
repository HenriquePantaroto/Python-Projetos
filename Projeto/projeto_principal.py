from Projeto import arquivos
from time import sleep
from Projeto.arquivos import titulo, menuUM, menuDOIS, menuTRES

listaProdutos = []

while True:
    titulo()
    menuUM()
    oper = str(input('\n\033[36mQual das operações acima você deseja executar: \033[m')).strip()
    if oper.isalpha():
        print('\n\033[36mDigite um número inteiro válido.\033[m')
    else:
        oper = int(oper)
        if oper >= 4:
            print('\n\033[36mEsta operação não existe, tente novamente.\033[m')
        elif oper == 1:
            menuDOIS()
            operUM = int(input('\n\033[36mQual das novas operações acima você deseja executar: \033[m'))
            if operUM == 1:
                while True:
                    listaProdutos.append(str(input('\n\033[36mQual o nome do produto: \033[m')))
                    listaProdutos.append(float(input('\033[36mQual o valor do produto: R$\033[m')))
                    continuar = str(input('\033[36mDeseja adicionar mais itens: [Sim/Sair] \033[m')).lower().strip()
                    if continuar == 'sair':
                        break
            elif operUM == 2:
                for n, i in listaProdutos:
                    print(f"[{n}] --- {listaProdutos[i]} --- R${listaProdutos[i+1]}")
            elif operUM == 3:
                for i in listaProdutos:
                    print(f'[{i}] --- {listaProdutos} --- R${listaProdutos} ')
                opcExc = int(input('\n\033[36mQual o número do item você quer excluir: \033[m')).strip()
                listaProdutos.pop(opcExc)
                listaProdutos.pop(opcExc+1)
            elif operUM == 4:
                continue
        elif oper == 2:
            menuTRES()
            operDOIS = str(input('\n\033[36mQual das novas operações acima você deseja executar: \033[m'))
            if operDOIS == 1:
                print('Em desenvolvimento.')
                #FORMA DE PAGAMENTO
            elif operDOIS == 2:
                print('Em desenvolvimento.')
                #DESCONTO
            elif operDOIS == 3:
                print('Em desenvolvimento.')
                #PRODUTOS
            elif operDOIS == 4:
                continue
        elif oper == 3:
            print('\nSAINDO DO PROGRAMA')
            break
sleep(1)
print('...')
sleep(1)
print('...')
sleep(1)
print('...')
sleep(1)
print('PROGRAMA ENCERRADO')
