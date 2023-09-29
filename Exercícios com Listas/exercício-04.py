"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

# Declarando uma lista de letras
listaLetras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# Comparando se a letra é vogal e removendo da lista
if ("a") in listaLetras:
    listaLetras.remove("a")
if ("e") in listaLetras:
    listaLetras.remove("e")
if ("i") in listaLetras:
    listaLetras.remove("i")
if ("o") in listaLetras:
    listaLetras.remove("o")
if ("u") in listaLetras:
    listaLetras.remove("u")

# Mostrando resultados
print(f"Foram lidas {len(listaLetras)} consoantes: {listaLetras}")
