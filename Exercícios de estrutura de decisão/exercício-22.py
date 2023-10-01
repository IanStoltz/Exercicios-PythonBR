'''Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).'''

# Coleta o número
num = int(input("Insira um número inteiro: "))

# Verifica se é par ou ímpar e mostra o resultado
if num % 2 == 0:
    print ("Número par")
else:
    print("Número ímpar")