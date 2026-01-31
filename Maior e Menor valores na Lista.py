#Exercício 1:
listanum = [] #Criando Lista vazia.
maior = 0 #Variável que vai guardar o maior número digitado pelo usuario.
menor = 0 #Variável que vai guardar o menor número digitado pelo usuario.

for c in range(0,5): #Estrutura for 
    #Lendo 5 números e adicionando eles a lista.
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0: #Se for a primeira leitura:
        maior = menor = listanum[c] #Maior e Menor vão receber o número digitado.
    else: #Se não
        if listanum[c] > maior: #Se o número digitado for maior que o numero que já está na variavel (maior):
            maior = listanum[c] #Maior vai receber esse novo número.
        
        elif listanum[c] < menor:  #Se não, se o número digitado for Menor que o número que já está na variavel (menor):
            menor = listanum[c] #Menor vai receber esse novo número.

print('-'*30)
print(f'Você digitou os seguintes valores {listanum}') 
print(f'O Maior valor digitado foi o {maior} nas posições ', end='')

#Valor e sua Posição na Lista
for pos, valores in enumerate(listanum):
    #Se algum valor na lista for igual ao que esta armazenado na variavel maior:
    if valores == maior:
        #Mostre as posições.
        print(f'{pos}...', end='') 

print() #Esse print ta separando as informações.

print(f'O Menor valor digitado foi o {menor} nas posições ', end='')
#Valor e sua Posição na Lista
for pos, valores in enumerate(listanum):
    #Se algum valor na lista for igual ao que esta armazenado na variavel menor:
    if valores == menor:
            #Mostre as posições.
            print(f'{pos}...', end='')