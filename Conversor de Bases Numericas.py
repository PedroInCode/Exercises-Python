# Python - Conversor de Bases Númericas

num = int(input("Digite um número inteiro: "))
print("""Escolha uma das Bases para conversão:
{ 1 } Converter para Binário
{ 2 } Converter para Octal
{ 3 } Converter para Hexadecimal""")
opcao = int(input("Sua opção: "))

if opcao == 1:
    print("{} Convertido para Binário é igual a {}".format(num, bin(num)[2:]))
elif opcao == 2:
    print("{} Convertido para Octal é igual a {}".format(num, oct(num)[2:]))
elif opcao == 3:
    print("{} Convertido para Hexadecimal é igual a {}".format(num, hex(num)[2:]))
else:
    print("Esta opção não existe!! Digite uma opção válida.")
    
    print("=============================================================")

    # Python - Comparando Números

num = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num > num2:
    print("O Primeiro número é MAIOR!!")
elif num2 > num:
    print("O Segundo número é MAIOR!!")
else: 
    print("Os dois números são IGUAIS!!")


