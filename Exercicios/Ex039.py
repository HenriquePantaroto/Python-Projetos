from time import sleep
idade = int(input('Digite a sua idade: '))
idadeIdeal = 17
tempo1 = idadeIdeal - idade
tempo2 = idade - idadeIdeal

print('\n\033[36mPROCESSANDO INFORMAÇÃO\033[m')
sleep(1)
print('\n\033[36m...\033[m')
sleep(1)
print('\n\033[36m...\033[m')
sleep(1)

if idade < idadeIdeal:
    print('\nVocê não tem idade suficiente para se alistar, ainda lhe falta {} ano(s).'.format(tempo1))
elif idade == 17:
    print('\nVocê tem a idade ideal para se alistar.')
else:
    print('\nVocê passou da idade de se alistar, já se passaram {} ano(s).'.format(tempo2))
