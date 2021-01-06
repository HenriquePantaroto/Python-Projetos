a = int(input('Digite o valor do primeiro lado: '))
b = int(input('Digite o valor do segundo lado: '))
c = int(input('Digite o valor do terceiro lado: '))

if a < b + c and b < a + c and c < b + a:
    if a == b and b == c and c == a:
        print('Este é um triangulo EQUILÁTERO.')
    elif a != b and b != c and c != a:
        print('Este é um triangulo ESCALENO.')
    else:
        print('Este é um triangulo ISOSCELES.')
else:
    print('Estes valores não formam um triangulo.')
