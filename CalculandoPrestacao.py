casa = float(input("Qual o Valor da Casa? R$"))
salario = float(input("Salário do Comprador: R$"))
anos = int(input("Quantos anos de financiamento? "))
prestação = casa / (anos * 12)
Minimo = salario * 30 / 100

print("Para pagar uma casa de {:.2f} em {} anos,".format(casa, anos), end = "") #end = "" --> serve para continuar escrevendo na mesma linha.
print(" a prestação será de R${:.2f}".format(prestação))

if prestação <= Minimo:
    print("Empréstimo pode ser concedido!")
else:
    print("Empréstimo Negado!!")