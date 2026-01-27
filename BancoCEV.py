print('-'*40)
print('{:^40}'.format('BANCO CEV')) 
print('-'*40)

valor = int(input('Que valor vc quer sacar? R$'))
total = valor
ced = 50
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de cedulas {totalced} de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('='*40)
print('Volte sempre ao Banco CEV! Tenha um Bom Dia!')
