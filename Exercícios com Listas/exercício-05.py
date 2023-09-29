"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""

# Declarando listas para armazenar os valores
num = []
par = []
impar = []

# Coletando os valores, classificando e inserindo na lista
for i in range(20):
    i += 1
    numero = int(input("Insira um número: "))
    num.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

# Mostrando resultados
print(f" Números inseridos: {num}")
print(f" Números pares: {par}")
print(f" Números ímpares: {impar}")
