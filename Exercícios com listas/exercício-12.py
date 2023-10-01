"""
Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos. 
"""

# Cria lista com idades e alturas
idades = [32, 89, 65, 34, 22, 34, 76, 12, 13, 29, 28, 54, 24]
alturas = [1.87, 1.65, 1.23, 1.89, 1.90, 1.32, 1.56, 1.87, 1.04, 1.21, 1.06, 1.76, 1.58]

# Calcula a média das alturas
media = sum(alturas) / len(alturas)

# Compara alturas dos menores de 13 com a média
quantidade = sum(1 for idade, altura in zip(idades, alturas) if idade > 13 and altura < media)

# Mostra os resultados
print(f"A quantidade de alunos abaixo da média {media:.2f} é de {quantidade} alunos")
