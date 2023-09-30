"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""

# Importa numpy para utilizar o método numpy.prod(lista)
import numpy

# Cria lista para armazenar os números
nums = []

# Coleta os números
for i in range(5):
    nums.append(int(input("Insira um número inteiro: ")))
    i += 1

# Calcula a soma e a multiplicação
soma = sum(nums)
multiplica = numpy.prod(nums)

# Mostra os resultados
print(f"Os números inseridos foram: {nums}")
print(f"A soma dos números é: {soma}, a multiplicação é: {multiplica}")
