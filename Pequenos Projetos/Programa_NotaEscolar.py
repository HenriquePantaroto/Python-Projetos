from time import sleep
nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
notaMedia = (nota1 + nota2) / 2
sleep(1)
print('\n\033[32mCalculando Média\033[m')
sleep(1)
print('\n\033[32m...\033[m')
sleep(1)
print('\n\033[32m...\033[m')
sleep(1)
if notaMedia < 5.0:
    print('\nSua nota média é {:.2f}, por isso você foi Reprovado. Estude mais.'.format(notaMedia))
elif notaMedia < 6.9:
    print('\nSua nota média é {:.2f}, por isso você está em Recuperação, prepare-se para sua prova.'.format(notaMedia))
else:
    print('\nParabéns, você foi Aprovado nesta matéria com uma nota média de {:.2f}.'.format(notaMedia))
