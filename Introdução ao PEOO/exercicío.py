#1------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

nome = input("Insira seu nome: ")
matr = input("Insira sua matrícula: ")
ano = matr[0:4]
semestre = matr[5]
curso = matr[6:10]
contador = matr[11:14]
print(f"Nome: {nome}")
print(f"Matrícula: {matr}")
print(f"Ano de ingresso: {ano}")

#2------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
for c in range(1, 11):
    nome = input("Insira seu nome: ")
for i in range(1, 11):
    matr = input("Insira sua matricula: ")
for b in range(1, 11):
    anodeingresso = matr[0:4]
for a in range(1, 11):
    print(f"Nome: {nome}")
    print(f"Matrícula: {matr}")  
    print(f"Ano de Ingresso no IFRN: {anodeingresso}")