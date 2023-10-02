'''Faça um programa que leia 5 números e informe o maior número.'''

# Declara lista para armazenar os números
numeros = []

# Coleta números no intervalo especificado e adiciona na lista
for i in range(5):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

# Obtem maior número
maior_numero = max(numeros)

# Mostra o resultado
print(f'O maior número é: {maior_numero}')