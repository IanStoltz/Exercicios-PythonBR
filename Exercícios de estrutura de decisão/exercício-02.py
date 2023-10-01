'''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.'''

# Coleta o número
num = int(input("Insira um número: "))

# Compara se é positivo ou negativo e mostra o resultado
if num > 0:
    print("É um número positivo")
elif num == 0:
    print("É zero")
else:
    print("É um número negativo")