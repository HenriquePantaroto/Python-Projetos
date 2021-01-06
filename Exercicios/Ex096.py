def area(largura, comprimento):
    are = largura * comprimento
    print(f'A área de um terreno {largura} X {comprimento} é de {are:.2f} metros quadrados.')


larg = float(input('Digite a Largura do Terreno: '))
compri = float(input('Digite o Comprimento do Terreno: '))
area(larg, compri)
