"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""

# Importando numpy para utilizar o método numpy.prod(lista)
import numpy

# Criando lista para armazenar os números
nums = []

# Coletando os números
for i in range(5):
    nums.append(int(input("Insira um número inteiro: ")))
    i += 1

# Calculando a soma e a multiplicação
soma = sum(nums)
multiplica = numpy.prod(nums)

# Mostrando os resultados
print(f"Os números inseridos foram: {nums}")
print(f"A soma dos números é: {soma}, a multiplicação é: {multiplica}")
