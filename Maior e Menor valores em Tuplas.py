from random import randint
from time import sleep

numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('-'*30)
print('Sorteando...')
sleep(2)
print(f'Os números sorteados foram:{numeros} ', end='')

#OUUUU

#for n in numeros:
    #print(f'{n} ', end='') 
    
print(f'\nO Maior número sorteado foi: {max(numeros)}')
print(f'O Menor número sorteado foi: {min(numeros)}')
print('-'*30)
