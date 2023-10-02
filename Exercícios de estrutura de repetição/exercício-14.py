'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.'''

# Declara variáveis para armazenar o total
par = 0
impar = 0

# Coleta 10 números inteiros, verifica se são pares ou ímpares e aumenta o valor total de cada
for _ in range(10):
    a = int(input("Insira um número inteiro: "))
    if a % 2 == 0:
        par += 1
    else:
        impar += 1

# Mostra o resultado
print(f'A quantidade de números pares é: {par} e a quantidade de ímpares é: {impar}')