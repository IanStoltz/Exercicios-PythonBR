'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''
# Resolvido sem o uso de if / else, método utilizando listas

# Declara lista para armazenar os valores
lista = []

# Coleta os números e inserindo na lista
for i in range(3):
    elemento = int(input("Insira um número: "))
    lista.append(elemento)

# Ordena lista de forma inversa ao mostrar o resultado
print(f'Os números inseridos em ordem decrescente são {lista[::-1]}')