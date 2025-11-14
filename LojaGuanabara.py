print('============== Loja Pedro ===============')
preço = float(input('\nPreço das Compras? R$'))
print('''\nFORMAS DE PAGAMENTO:
 { 1 } À Vista dinheiro/cheque
 { 2 } À Vista no cartão
 { 3 } 2x no cartão
 { 4 } 3x ou mais no cartão''')
Escolha = int(input('Qual a forma de pagamento? '))

if Escolha == 1:
    total = preço - (preço * 10 / 100)
    print('Sua Compra de R${} recebeu um desconto!! O Valor passou a ser R${}'.format(preço, total))
elif Escolha == 2:
    total = preço - (preço * 5 / 100)
    print('Sua Compra de R${} recebeu um desconto!! O Valor passou a ser R${}'.format(preço, total))

elif Escolha == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros.'.format(parcela))

elif Escolha == 4:
    parcelas = int(input('Quantas vezes deseja parcelar? '))
    total = preço + (preço * 20 / 100)
    valorparcela = total / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(parcelas, valorparcela ))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))

else:
    print('Escolha uma Forma de Pagamento Válida!')
