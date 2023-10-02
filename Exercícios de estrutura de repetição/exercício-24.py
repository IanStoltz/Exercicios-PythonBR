'''Faça um programa que calcule o mostre a média aritmética de N notas.'''

# Coleta quantas notas serão inseridas
n = int(input("Digite N: "))

# Declara lista para armazenar as notas
todasAsNotas = []

# Itera pelo N inserido, coleta notas e insere na lista
for _ in range(n):
    nota = float(input("Digite uma nota: "))
    todasAsNotas.append(nota)

# Calcula a média
media = sum(todasAsNotas) / n

# Mostra o resultado
print(f'A média é de: {media}')