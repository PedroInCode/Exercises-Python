n1 = float(input("Qual foi sua primeira Nota? "))
n2 = float(input("Qual foi sua segunda nota? "))

média = (n1 + n2) / 2

print("Sua Média foi de {}".format(média))

if média >= 7:
    print("Você está APROVADO!! Meus Parabéns!!")
elif média >= 5 and média < 7:
    print("Você está de RECUPERAÇÃO!!")
elif média < 5:
    print("Você está REPROVADO!!")
