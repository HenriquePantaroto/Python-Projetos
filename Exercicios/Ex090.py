dicionario = {}

dicionario['nome'] = str(input('Digite o nome do aluno: '))
dicionario['media'] = float(input(f'Qual a média de {dicionario["nome"]}: '))
dicionario['situação'] = 'Aprovado', 'Reprovado', 'Recuperação'
print('-=' * 30)
print(f' --> Nome é igual à {dicionario["nome"]}.')
print(f' --> Média é igual à {dicionario["media"]}.')

if dicionario['media'] <= 5:
    print(f' --> Situação é igual à {(dicionario["situação"][1])}.')
elif dicionario['media'] <= 6:
    print(f' --> Situação é igual à {(dicionario["situação"][2])}.')
else:
    print(f' --> Situação é igual à {(dicionario["situação"][0])}.')

print()
print('FIM de Operação')
