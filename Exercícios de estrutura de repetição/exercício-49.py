'''
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.
'''

# Coleta o número de termos
n = int(input("Digite o número de termos da série: "))

# Declara variável para soma e contador
soma = 0
m = 1

# Itera pelo intervalo proposto e incrementa a variável
for i in range(1, n+1):
    soma += i/m
    m += 2

# Mostra resultado da série no intervalo proposto
print("A série é:")
for i in range(1, n+1):
    print(f"{i}/{2*i-1}", end=" ")
print()

# Mostra o resultado da soma
print(f'A soma dos termos da série é: {soma:.2f}')