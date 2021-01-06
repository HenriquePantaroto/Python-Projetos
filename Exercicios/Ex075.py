num1 = int(input('Digite o primeiro valor: [1/10] '))
while num1 > 10:
     num1 = int(input('Digite novamente: [1/10] '))
num2 = int(input('Digite o primeiro valor: [1/10] '))
while num2 > 10:
     num2 = int(input('Digite novamente: [1/10] '))
num3 = int(input('Digite o primeiro valor: [1/10] '))
while num3 > 10:
     num3 = int(input('Digite novamente: [1/10] '))
num4 = int(input('Digite o primeiro valor: [1/10] '))
while num4 > 10:
     num4 = int(input('Digite novamente: [1/10] '))

lista = (num1, num2, num3, num4)
numPares = 0

print(f'O número Nova apareceu {lista.count(9)} vezes.')

if 3 in lista:
    print(f'O número Três apareceu na {lista.index(3) + 1}º posição.')
else:
    print('O número 3 não foi digitado')

if num1 % 2 == 0:
     numPares += 1
if num2 % 2 == 0:
     numPares += 1
if num3 % 2 ==0:
     numPares += 1
if num4 % 2 == 0:
     numPares += 1
print(f'A quantidade de números pares foi: {numPares}')


######################## Outra Solução ################################

lista = (int(input('Digite o primeiro valor: [1/10] ')),
int(input('Digite o primeiro valor: [1/10] ')),
int(input('Digite o primeiro valor: [1/10] ')),
int(input('Digite o primeiro valor: [1/10] ')))

numPares = 0

print(f'O número Nova apareceu {lista.count(9)} vezes.')

if 3 in lista:
    print(f'O número Três apareceu na {lista.index(3) + 1}º posição.')
else:
    print('O número 3 não foi digitado')

for n in lista:
     if n % 2 == 0:
          numPares += 1

print(f'A quantidade de números pares foi: {numPares}')
