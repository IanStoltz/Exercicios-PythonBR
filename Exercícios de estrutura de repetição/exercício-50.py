'''Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.'''

# Coleta o número de termos
n = int(input("Digite o número de termos: "))
h = 0

# Itera pelo intervalo especificado
for i in range(1, n+1):
    h += 1/i

# Mostra o resultado
print(f'O valor de H com {n} termos é: {h:.2f}')