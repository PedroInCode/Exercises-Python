print('Digite 4 Números abaixo:')
numeros = (int(input('N1: ')), int(input('N2: ')), int(input('N3: ')), int(input('N4: ')))

print('-'*40)
print(f'Você digitou os seguintes números: {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
print(f'O número 3 apareceu na {numeros.index(3)+1}ª posição.')
print('Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end='')




