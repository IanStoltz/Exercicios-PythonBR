"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
"""
# Importa numpy
import numpy as np

# Cria uma lista para armazenar os valores
nums = []

# Coleta os valores e armazena na lista
for i in range(10):
    nums.append(int(input("Insira um número inteiro: ")))

# Calcula o quadrado usando numpy e realiza a soma dos valores
quadrados = np.square(nums)
soma = np.sum(quadrados)

# Mostra os resultados
print(f"Os números inseridos foram: {nums}")
print(f"A soma dos quadrados dos números é: {soma}")
