idade = int(input('Digite a sua idade para saber sua categoria: '))

if idade <= 9:
    print('Sua categoria é a MIRIM.')
elif idade <= 14:
    print('Sua categoria é a INFANTIL.')
elif idade <= 19:
    print('Sua categoria é a JÚNIOR.')
elif idade <= 20:
    print('Sua categoria é a SÊNIOR.')
else:
    print('Sua categoria é a MASTER.')