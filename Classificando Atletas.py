from datetime import date
anoAtual = date.today().year
nascimento = int(input("Em que ano vc nasceu? "))

idade = anoAtual - nascimento

print("O atleta têm {} anos.".format(idade))
if idade < 10:
    print("Classificação: Mirim")
elif idade >= 10 and idade <= 20:
    print("Classificação: Junior")
elif idade > 20:
    print("Classificação: Sênior")