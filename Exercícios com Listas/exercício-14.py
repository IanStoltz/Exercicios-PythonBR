"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: 
"Telefonou para a vítima?" "Esteve no local do crime?" "Mora perto da vítima?" "Devia para a vítima?" "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""

# Criando lista para armazenar as respostas
respostas = []

# Iniciando questionamentos e armazenando resposta na lista
print("Interrogatório. Digite S para sim e N para não")
p1 = input("Telefonou para a vítima? ")
if p1 == "S" or p1 == "s":
    respostas.append(p1)
p2 = input("Esteve no local do crime? ")
if p2 == "S" or p2 == "s":
    respostas.append(p2)
p3 = input("Mora perto da vítima? ")
if p3 == "S" or p3 == "s":
    respostas.append(p3)
p4 = input("Mora perto da vítima? ")
if p4 == "S" or p4 == "s":
    respostas.append(p4)
p5 = input("Mora perto da vítima? ")
if p5 == "S" or p5 == "s":
    respostas.append(p5)

# Comparando número de respostas, classificando e mostrando o resultado
if len(respostas) == 5:
    print("Assassino")
elif len(respostas) <= 4 and len(respostas) >= 3:
    print("Cúmplice")
elif len(respostas) < 3 and len(respostas) > 1:
    print("Suspeito")
else:
    print("Inocente")
