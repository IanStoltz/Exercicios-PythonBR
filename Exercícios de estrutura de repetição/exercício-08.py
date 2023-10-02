'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''

# Decla lista para armazenar os números
numeros = []

# Coleta números no intervalo especificado e adiciona na lista
for i in range(5):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

# Calcula a soma e a média
soma = sum(numeros)
media = soma / len(numeros)

# Mostra os resultados
print(f'A soma dos números é: {soma} e a média é: {media}')
