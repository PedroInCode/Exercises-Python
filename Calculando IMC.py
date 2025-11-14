peso = float(input("Qual é o seu peso? (KG) "))
altura = float(input("Qual é a sua altura? (M) "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Vc está ABAIXO DO PESO normal!!')
elif 18.5 <= imc < 25:
    print('Parabéns, vc está na faixa de PESO NORMAL!!')
elif 25 <= imc < 30:
    print('Vc está em SOBREPESO!!')
elif 30 <= imc < 40:
    print('Vc está em OBESIDADE!! CUIDADO.')
elif imc >= 40:
    print('Vc está em OBESIDADE MÓRBIDA!! CUIDADO!!')
