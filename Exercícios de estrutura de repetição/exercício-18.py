'''Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.'''

# Coletan o valor de N e declarando lista para armazenar os valores
n = int(input("Digite N: "))
numeros = []

# Itera N vezes, coleta os valores e inserindo na lista
for i in range(n):
    x = float(input("Digite um número: "))
    numeros.append(x)

# Calcula maior e menor número
maior = max(numeros)
menor = min(numeros)

# Calcula a soma
soma = maior + menor

# Mostra o resultado
print(f'O maior valor digitado foi {maior} e o menor foi {menor}, a soma é de: {soma}')