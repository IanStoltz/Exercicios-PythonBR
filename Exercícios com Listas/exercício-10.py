"""
Faça um Programa que leia dois vetores com 10 elementos cada. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""

# Declarando listas para armazenar valores
lista1 = []
lista2 = []
lista3 = []

# Coletando elementos para as listas
for i in range(10):
    i += 1
    num = input("Insira um elemento na primeira lista: ")
    lista1.append(num)
    lista3.append(num)
    num1 = input("Insira um elemento na segunda lista: ")
    lista2.append(num1)
    lista3.append(num1)

# Mostrando os resultados
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista intercalada: {lista3}")
