"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

# Declarando uma lista para armazenar as notas
listaNotas = []

# Coletando as notas
for i in range(4):
    i += 1
    nota = float(input(f"Insira sua {i}ª nota: "))
    listaNotas.append(nota)

# Calculando a média
media = sum(listaNotas) / len(listaNotas)

# Mostrando os resultados
print(f"Suas notas foram: {listaNotas}")
print(f"Sua média das quatro notas é: {media}")
