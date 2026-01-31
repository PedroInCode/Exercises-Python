num = [0, 3, 5, 7]
num[2] = 4 #Alterando um elemento da lista -> 5 SAI e ENTRA o 4
num.append(8) #Adicionando um novo elemento a lista.
num.sort() #Organizando minha lista da maneira padrão: Menor -> Maior 
num.insert(2, 9) #Inserindo um novo elemento (9) na posição 2 da lista.
#num.sort(reverse=True) ----- Organizando a lista da maneira reversa: Maior -> Menor
num.pop(5)  #Deletando o elemento que esta na posição 5 da lista. É o 8!
if 7 in num: #Se houver o número 8 na lista num:
    num.remove(7) #Remova o numero 8.
    print('Encontrei o número 7 na Lista e já removi como solicitado.')
else: #SENÃO
    print('Não encontrei o número 8 na lista!')

print(num)
#Mostrando o número de elementos armazenados na lista.
print(f'Essa lista tem {len(num)} elementos armazenados.') 

