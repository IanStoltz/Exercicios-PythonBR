"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
"""
# Importando numpy
import numpy as np

# Criando uma lista para armazenar os valores
nums = []

# Coletando os valores e armazenando na lista
for i in range(10):
    nums.append(int(input("Insira um número inteiro: ")))

# Calculando o quadrado usando numpy e realizando a soma dos valores
quadrados = np.square(nums)
soma = np.sum(quadrados)

# Mostrando os resultados
print(f"Os números inseridos foram: {nums}")
print(f"A soma dos quadrados dos números é: {soma}")
