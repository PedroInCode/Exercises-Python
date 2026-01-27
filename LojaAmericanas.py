totcompra = maisQmil = maisBarato = contador = 0
prodMaisBarato = ' '

print('-'*40)
print('AMERICANAS')
print('-'*40)

while True:
    produto = str(input('Nome do Produto: ')).strip().upper()
    preco = float(input('Preço: R$'))
    totcompra += preco

    if preco > 1000:
        maisQmil += 1
    contador += 1

    if contador == 1:
        maisBarato = preco
        prodMaisBarato = produto
    else:
        if preco < maisBarato:
            maisBarato = preco
            prodMaisBarato = produto

    cont = ' '
    while cont not in 'SN':
        print('-'*40)
        cont = str(input('Quer Continuar? [S/N]')).strip().upper()[0]
    if cont == 'N':
        print('{:-^40}'.format('PROGRAMA ENCERRADO'))
        break

print(f'O total da compra foi R${totcompra:.2f} .')
print(f'Temos {maisQmil} produto custando mais de R$1000,00 .')
print(f'O produto mais barato foi {prodMaisBarato} que custou R${maisBarato:.2f} .')