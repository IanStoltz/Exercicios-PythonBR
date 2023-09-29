# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

# Declarando listas para armazenar valores
lista1 = []
lista2 = []
lista3 = []
lista4 = []

# Coletando elementos para as listas
for i in range(10):
    i += 1
    num = input("Insira um elemento na primeira lista: ")
    lista1.append(num)
    lista4.append(num)
    num1 = input("Insira um elemento na segunda lista: ")
    lista2.append(num1)
    lista4.append(num1)
    num = input("Insira um elemento na terceira lista: ")
    lista3.append(num)
    lista4.append(num)

# Mostrando os resultados
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista 3: {lista3}")
print(f"Lista intercalada: {lista4}")
