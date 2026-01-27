soma = quantidade = media = 0
sn = 'S'

while sn in 'Ss':
    n = int(input('Digite um valor: '))
    soma += n
    quantidade += 1
    
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior: 
            maior = n
        elif n < menor:
            menor = n
        elif n == maior:
            maior = n
        elif n == menor:
            menor = n

    sn = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

media = soma / quantidade
print('Vc digitou {} numeros e a media foi {}'.format(quantidade, media))
print('O maior numero foi {} e o menor foi {}'.format(maior, menor))
