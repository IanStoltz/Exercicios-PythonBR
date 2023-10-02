'''Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.'''

# Coleta o valor de N e declara lista para armazenar os valores
n = int(input("Digite N: "))
numeros = []

# Itera N vezes, coleta os valores e insere na lista
for i in range(n):
    x = float(input("Digite um número: "))
    
    # Verifica se o número está no intervalo proposto
    while x < 0 or x > 1000:
       x = float(input("Digite um número entre 0 e 1000: "))
    numeros.append(x)

# Calcula maior e menor número
maior = max(numeros)
menor = min(numeros)

# Calcula a soma
soma = maior + menor

# Mostra o resultado
print(f'O maior valor digitado foi {maior} e o menor foi {menor}, a soma é de: {soma}')