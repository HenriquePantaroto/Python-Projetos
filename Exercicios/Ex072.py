numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
num = int(input('Digite um número de 0 à 20: '))
oper = ''
while num > 20:
    num = int(input('Número inválido, tente novamente: '))
print(f'O número que você digitou foi o {numeros[num]}')

while oper != 'sair':
    oper = str(input('Você deseja continuar? [Sim/Sair] ')).strip().lower()
    if oper == 'sair':
        break
    num = int(input('Digite um número de 0 à 20: '))
    while num > 20:
        num = int(input('Número inválido, tente novamente: '))
    print(f'O número que você digitou foi o {numeros[num]}')

print('Fim do Programa!')
