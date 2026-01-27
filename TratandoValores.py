num = soma = cont = 0
num = int(input('Digite um numero [999 para parar!]: ')) #Posso digitar 999, porem nao vai resultar em nada!! Ja que o cont e soma entao dentro de uma estrutura, e essa estrutura tem uma verificacao ( num != 999).

while num != 999: #Enquanto o num for diferente de 999:
    cont += 1 # A cada numero digitado o cont vai receber +1
    soma += num # Vai sempre somar os numeros digitados.
    num = int(input('Digite um numero [999 para parar!]: ')) #Quando eu digitar 999 o num nao vai receber o valor 999, pois para num receber algum valor ele tem que passar pela verificacao!

print('Vc digitou {} numeros e o total foi {}.'.format(cont, soma))
print('Fim.')
