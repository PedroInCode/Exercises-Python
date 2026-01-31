palavras = ('santos','corinthians', 'sao paulo', 'palmeiras', 'internacional','gremio', 'flamengo', 'fluminense')

for p in palavras: #Para cada p(palavra) dentro da variavel composta 'palavra':

    #{p.upper} -> Deixa a palavra inteira em letra maiúscula para destacar.
    print(f'\nNa palavra {p.upper} temos as Vogais: ', end='')

    #Para cada letra em cada p(palavra):
    for letra in p:

        #Se letra for 'a' 'e' 'i' 'o' ou 'u':
        # .lower deixa as letras minúsculas para cair no sistema de identificação -> 'aeiou'.
        if letra.lower() in 'aeiou': 

            #Escreva a letra.
            print(f'{letra} ', end='')

#Caso as letras 'aeiou' tenham pontuação, é necessario adicionar no sistema de verificacão -> 'aàáãâeéêè.. Em diante.