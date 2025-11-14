import random

n1 = str(input("Primeiro Aluno: "))
n2 = str(input("Segundo Aluno: "))
n3 = str(input("Terceiro Aluno: "))
n4 = str(input("Quarto Aluno: "))

lista_set = {n1, n2, n3, n4}
lista_para_sorteio = list(lista_set)
escolhido = random.choice(lista_para_sorteio)

print("O aluno sorteado foi o(a) {}".format(escolhido))