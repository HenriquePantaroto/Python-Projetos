frase = input('Digite uma frase: ').strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('A frase {}, é um palíndromo: {}'.format(junto, inverso))
else:
    print('A frase {}, não é um palíndromo: {}'.format(junto, inverso))