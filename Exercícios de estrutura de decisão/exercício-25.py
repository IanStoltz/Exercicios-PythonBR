'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
 Caso contrário, ela será classificado como "Inocente".
'''

print("Interrogatório, responda sim ou não")

# Coleta respostas das perguntas e declara variável que armazena o total de respostas positivas
pergunta = str(input("Telefonou para a vítima? "))
pergunta1 = str(input("Esteve no local do crime? "))
pergunta2 = str(input("Mora perto da vítima? "))
pergunta3 = str(input("Devia para a vítima? "))
pergunta4 = str(input("Já trabalhou com a vítima? "))
num_respostas = 0

# Verifica as respostas e incrementa a variável em caso positivo
for resposta in [pergunta, pergunta1, pergunta2, pergunta3, pergunta4]:
    if resposta.lower() == "sim":
        num_respostas += 1

# Compara número de respostas e mostra o resultado
if num_respostas == 5:
    print("Assassino")
elif 3 <= num_respostas < 5:
    print("Cúmplice")
elif num_respostas == 2:
    print("Suspeito")
else:
    print("Inocente")