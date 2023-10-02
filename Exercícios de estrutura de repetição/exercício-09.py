'''Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.'''

# Mostra o resultado se número do intervalo for ímpar
num = 0
while num <= 49:
    num += 1
    if num % 2 == 0:
        continue
    else:
        print(num)

# Resolução mais simples com for, iterando a sequência com passo de 2 (apenas números ímpares)
for num in range(1, 50, 2):
    print(num)