"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: 
"Telefonou para a vítima?" "Esteve no local do crime?" "Mora perto da vítima?" "Devia para a vítima?" "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""

# Criando uma lista para armazenar as respostas
respostas = []

# Iniciando o interrogatório e armazenando as respostas na lista
print("Interrogatório. Digite S para sim e N para não")
p1 = input("Telefonou para a vítima? ")
if p1.lower() == "s":
    respostas.append(p1)
p2 = input("Esteve no local do crime? ")
if p2.lower() == "s":
    respostas.append(p2)
p3 = input("Mora perto da vítima? ")
if p3.lower() == "s":
    respostas.append(p3)
p4 = input("Devia para a vítima? ")
if p4.lower() == "s":
    respostas.append(p4)
p5 = input("Já trabalhou com a vítima? ")
if p5.lower() == "s":
    respostas.append(p5)

# Comparando o número de respostas, classificando e mostrando o resultado
if len(respostas) == 5:
    print("Assassino")
elif 3 <= len(respostas) <= 4:
    print("Cúmplice")
elif 1 < len(respostas) < 3:
    print("Suspeito")
else:
    print("Inocente")
