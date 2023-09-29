"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

# Declarando uma lista de letras
listaLetras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# Criando uma lista de vogais
vogais = ["a", "e", "i", "o", "u"]

# Removendo as vogais da lista de letras
for vogal in vogais:
    if vogal in listaLetras:
        listaLetras.remove(vogal)

# Mostrando resultados
print(f"Foram lidas {len(listaLetras)} consoantes: {listaLetras}")
