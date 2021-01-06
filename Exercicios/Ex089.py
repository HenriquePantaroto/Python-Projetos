from time import sleep
oper = ''
lista = []
listaNomes = []
count = 0
while oper != 'sair':
    listaNomes.append(str(input('Digite o nome do aluno: ')))
    listaNomes.append(float(input('Digite a nota 1 do aluno: ')))
    listaNomes.append(float(input('Digite a nota 2 do aluno: ')))
    count += 1
    sleep(1.5)
    oper = str(input('Deseja continuar? [Sim/Sair] ')).strip().lower()
    lista.append(listaNomes[:])
    listaNomes.clear()
print()
sleep(2)
print('\033[31m-=' * 5, 'BOLETIM COM MÉDIA', '-=\033[m' * 5)
print()
opera = ''
while opera != 'sair':
    for n in range(0, count):
        media = (lista[n][1] + lista[n][2]) / 2
        print(f'\033[35mNúmero:\033[m [{n}] \033[35mAluno:\033[m [{lista[n][0]}] \033[35mMédia:\033[m [{media:.2f}]')
    print()
    sleep(1.5)
    aluno = int(input('\nDigite qual aluno você deseja ver as notas: '))
    print(f'\nO aluno {lista[aluno][0]} tirou nas provas: {lista[aluno][1]} e {lista[aluno][2]}')
    opera = str(input('\nVocê quer ver outras notas? [Sim/Sair] ')).strip().lower()
    if opera == 'sair':
        break
sleep(1)
print('Encerrando programa ...')
sleep(1)
print('...')
sleep(1)
print('...')
sleep(1)
print('Fim do Programa!')
