"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""

# Declarando listas para armazenar os valores
numeros = []
pares = []
impares = []

# Coletando os valores, classificando e inserindo na lista
for i in range(20):
    numero = int(input("Insira um número: "))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Mostrando resultados
print(f"Números inseridos: {numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
