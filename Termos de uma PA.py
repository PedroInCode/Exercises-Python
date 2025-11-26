print('-=' * 15)
print('     10 Termos de uma PA     ')
print('-=' * 15)

termoUM = int(input('\nPrimeiro Termo: '))
razao = int(input('Razão: '))
decimo = termoUM + (10-1) * razao

for c in range(termoUM, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU!!')