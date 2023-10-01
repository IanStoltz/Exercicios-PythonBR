"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

# Declara uma lista de letras
listaLetras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# Cria uma lista de vogais
vogais = ["a", "e", "i", "o", "u"]

# Remove as vogais da lista de letras
for vogal in vogais:
    if vogal in listaLetras:
        listaLetras.remove(vogal)

# Mostra o resultado
print(f"Foram lidas {len(listaLetras)} consoantes: {listaLetras}")
