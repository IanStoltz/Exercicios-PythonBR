'''
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . 
Depois, mostre quantas vezes cada valor foi conseguido. 
Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
'''

# Importando random para gerar números aleatórios
import random

# Gerando lista de números
numeros = [0] * 6

# Lançando 100 vezes e adicionando nas listas
for _ in range(1, 100):
    n = random.randint(1, 6)
    numeros[n - 1] += 1

# Mostrando resultados
for i, n in enumerate(numeros):
    print(f'O número {i+1} foi lançado {n} vezes.')