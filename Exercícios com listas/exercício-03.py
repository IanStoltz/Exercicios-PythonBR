"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

# Declara uma lista para armazenar as notas
listaNotas = []

# Coleta as notas
for i in range(4):
    i += 1
    nota = float(input(f"Insira sua {i}ª nota: "))
    listaNotas.append(nota)

# Calcula a média
media = sum(listaNotas) / len(listaNotas)

# Mostra os resultados
print(f"Suas notas foram: {listaNotas}")
print(f"Sua média das quatro notas é: {media}")
