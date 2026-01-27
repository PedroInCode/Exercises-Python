print('-='*40)
print('Vamos Jogar Par ou Impar')
print('-='*40)

from random import randint
v = 0

while True:
    valor = int(input('Digite um Valor de 0 a 10: '))
    pc = randint(0, 11)
    s = valor + pc
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    print('-'*80)
    print(f'Vc jogou {valor} e o computador jogou {pc}. Total de {s}')
    print('-'*80)

    if tipo == 'P':
        if s % 2 == 0:
            print('Vc Venceu!!!')
            v += 1
            print('-='*40)
        else:
            print('Vc Perdeu')
            print('-='*40)
            print(f'GAME OVER! Vc venceu {v} vezes.')
            break

    elif tipo == 'I':
        if s % 2 == 1:
            print('Vc Venceu!!!')
            v += 1
            print('-='*40)
        else:
            print('Vc Perdeu!!!')
            print('-='*40)
            print(f'GAME OVER! Vc venceu {v} vezes.')
            break

    print('Vamos Jogar Novamente...')
    print(f'Vc venceu {v} vezes.')
