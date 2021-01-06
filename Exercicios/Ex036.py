from time import sleep

valorCasa = float(input('Digite o valor da casa R$'))
salario = float(input('\nDigite o valor do seu salário R$'))
anos = int(input('\nDigite em quantos anos você pretende pagar a casa: '))

print('\033[36mPROCESSANDO INFORMAÇÕES\033[m')
sleep(2)
print('\033[36m...\033[m')
sleep(2)
print('\033[36m...\033[m\n')
sleep(2)

mensalidade = valorCasa / (anos * 12)
trintaPorcento = salario * (30 / 100)

print('\nA mensalidade nestas condições é de \033[31mR${:.2f}\033[m.'.format(mensalidade))
sleep(1)
print('\nOs 30% do seu salário correspondem a \033[31mR${:.2f}\033[m.'.format(trintaPorcento))
sleep(1)

if mensalidade <= trintaPorcento:
    print('\nSeu financiamento foi aprovado com sucesso. A mensalidade a ser paga é de \033[32mR${:.2f}\033[m por mês.'.format(mensalidade))
else:
    print('\nO seu financiamento não foi aprovado. A mensalidade ultrapassa 30% do seu salário mensal.')
