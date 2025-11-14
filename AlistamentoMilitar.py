from datetime import date

anoAtual = date.today().year
nascimento = int(input("Qual o ano do seu nascimento? "))
idade = anoAtual - nascimento
print("Quem nasceu em {} tem {} anos em {}.".format(nascimento, idade, anoAtual))

if idade == 18:
    calculo = 18 - idade
    print("Você já tem {} anos! Vc deve se alistar!!".format(idade))
elif idade < 18:
    print("Você ainda não tem 18 anos! Faltam {} anos para vc poder se alistar.".format(calculo))   
elif idade > 18:
    calculo = idade - 18
    print("Você já deveria ter se alistado há {} anos!!!".format(calculo)) 
