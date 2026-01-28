cont = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
while True:
    num = int(input('Digite um número entre 0 e 10: '))
    if 0 <= num <= 20:
        break
    print('Tente Novamente. ', end='')
print(f'Voce digitou o número {cont[num]}.')