#Exemplo 1
'''for teste in range( 1, 10):
    print(teste)
print('Fim')'''

#Exemplo 2
'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')'''

#Teste da Condição While:
'''r = 'S'
while r == 'S':
    n = int(input('Digite um Valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')'''

#Primeiro Exercício:

par = impar = 0
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números impares.'.format(par, impar))