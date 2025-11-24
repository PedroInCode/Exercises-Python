#Pedra, Papel ou Tesoura

from random import randint #Serve para sortear um número aleatório
from time import sleep #Serve para adicionar temporizador

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas Opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
escolha = int(input("Qual a sua Jogada? ")) 
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print("-=" * 10)
print('O Computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[escolha]))
print('-=' * 10)

if computador == 0: #Computador jogou Pedra
    if escolha == 0:
        print('EMPATE')
    elif escolha == 1:
        print('JOGADOR VENCE')
    elif escolha == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada Inválida!!')
elif computador == 1: #Computador jogou Papel
    if escolha == 0:
        print('COMPUTADOR VENCE')
    elif escolha == 1:
        print('EMPATE')
    elif escolha == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada Inválida!!')

elif computador == 2: #Computador jogou Tesoura
    if escolha == 0:
        print('JOGADOR VENCE')
    elif escolha == 1:
        print('COMPUTADOR VENCE')
    elif escolha == 2:
        print('EMPATE')
    else:
        print('Jogada Inválida')





