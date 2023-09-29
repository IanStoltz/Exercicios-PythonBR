"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.
"""

# Declarando variáveis e listas para armazenar valores
alunos = 1
todasMedias = []
medias7 = []

# Estabelecendo limite de entradas
while alunos <= 10:
    print(f"Aluno {alunos}")
    notas = []
    for i in range(4):
        # Coletando as 4 notas de cada aluno e classificando a média
        nota = float(input(f"Insira sua {i+1}ª nota: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    todasMedias.append(media)
    if media >= 7:
        medias7.append(media)
    alunos += 1

# Mostrando resultados
alunos7 = len(medias7)
print(f"O número de alunos com média maior ou igual a 7 é de: {alunos7}")
