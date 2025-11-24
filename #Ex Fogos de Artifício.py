#Ex Fogos de Artifício

from time import sleep


for c in range(10, 0-1, -1):
    print(c)
    sleep(1)
print("FELIZ ANO NOVO!!!")

#Ex Números Pares

for c in range(2, 50+1, +2):
    print(c)
    sleep(1)

#Ex Tabuada

num = int(input('Digite um Número: '))
print("-=" * 10)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))