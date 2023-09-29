"""
Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos. 
"""

# Gerando lista de idades e alturas
idades = [32, 89, 65, 34, 22, 34, 76, 12, 13, 29, 28, 54, 24]
alturas = [1.87, 1.65, 1.23, 1.89, 1.90, 1.32, 1.56, 1.87, 1.04, 1.21, 1.06, 1.76, 1.58]
i = 0
c = 0
quantidade = 0

# Calculando media das alturas
while i < len(alturas):
    i += 1
media = sum(alturas) / len(alturas)

# Comparando alturas dos menores de 13 com a média
while c < len(idades):
    if idades[c] > 13 and alturas[c] < media:
        quantidade += 1
    c += 1

# Mostrando os resultados
print(f"A quantia de alunos abaixo da média {media:.2f} é de {quantidade} alunos")
