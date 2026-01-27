num = int(input('\033[mDigite um Numero: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} ' .format(c), end ='')
print('\n\033[mO número {} foi dividido {} vezes.'.format(num, tot))
if tot == 2:
    print('E por isso ele \033[32mÉ \033[mum número \033[34mprimo.')
else:
    print('E por isso ele \033[31mNÃO \033[mé um número \033[34mprimo.')