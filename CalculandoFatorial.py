from math import factorial
from time import sleep

n = int(input('Digite um número para calcular o seu Fatorial: '))
f = factorial(n)
c = n
print('>>>>Calculando {}! = '.format(n), end='')
sleep(1)

while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print('{}'.format(f))