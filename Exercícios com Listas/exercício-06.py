"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.
"""

# Declarando variáveis e listas para armazenar valores
alunos = 1
listaNotas = []
todasMedias = []
medias7 = []

# Estabelecendo limite de entradas
while alunos <= 10:
    print(f"Aluno {alunos}")
    for i in range(4):
        i += 1
        # Coletando as 4 notas de cada aluno e classificando a média
        listaNotas.append(float(input(f"Insira sua {i}ª nota: ")))
        if len(listaNotas) == 4:
            media = sum(listaNotas) / 4
            todasMedias.append(media)
            if media >= 7:
                medias7.append(media)
            listaNotas.clear()
    alunos += 1
alunos7 = len(medias7)

# Mostrando resultados
print(f"O número de alunos com média maior ou igual a 7 é de: {alunos7}")
