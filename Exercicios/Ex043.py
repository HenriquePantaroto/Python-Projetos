peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura**2)

if imc < 18.5:
    print('Seu IMC é {:.2f}, e você está abaixo do seu peso ideal.'.format(imc))
elif imc < 25:
    print('Seu IMC é {:.2f}, e você está dentro do peso ideal.'.format(imc))
elif imc < 30:
    print('Seu IMC é {:.2f}, e você está acima do seu peso ideal.'.format(imc))
elif imc < 40:
    print('Seu IMC é {:.2f}, e você está na faixa de Obesidade.'.format(imc))
else:
    print('Seu IMC é {:.2f}, e você está na faixa de Obesidade Mórbida.'.format(imc))
