def notas(* num, situ=False):
    """
    A função 'notas' é uma função que traz informações relevantes sobre os números digitados.
    :param num: Quantidade infinita de números que representam as notas dos alunos.
    :param situ: Caso seja True, mostra a situação da sala em relação a média das notas.
    :return:
    """
    numTot = 0
    dicionario = {}
    dicionario['quant'] = len(num)
    print('-=' * 25)
    print(f'Quantidade: {dicionario["quant"]}')
    dicionario['maior'] = max(num)
    print(f'Maior: {dicionario["maior"]}')
    dicionario['menor'] = min(num)
    print(f'Menor: {dicionario["menor"]}')
    dicionario['media'] = sum(num) / len(num)
    print(f'Média: {dicionario["media"]:.2f}')
    dicionario['situação'] = 'RUIM', 'RAZOÁVEL', 'BOA'
    if situ:
        if dicionario['media'] < 5:
            print(f'Situação: {dicionario["situação"][0]}')
        elif dicionario['media'] <= 6:
            print(f'Situação: {dicionario["situação"][1]}')
        else:
            print(f'Situação: {dicionario["situação"][2]}')


#Criar uma maneira do usuário digitar os números dentro da função.

notas(5.5, 7, 8, 9, situ=True)
print('-=' * 25)
help(notas)
