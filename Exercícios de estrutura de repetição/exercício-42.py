'''
Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos:
[0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
'''

# Declara variáveis para armazenar o total em cada intervalo
intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0

# Coleta os números, compara os valores e atribuí nas variáveis ou encerra o programa
while True:
    num = int(input("Insira um número inteiro (um negativo para o programa): "))
    if num < 0:
        break
    if num <= 25:
        intervalo1 += 1
    elif num <= 50:
        intervalo2 += 1
    elif num <= 75:
        intervalo3 += 1
    elif num <= 100:
        intervalo4 += 1
    else:
        print ("Número inválido")

# Mostra os resultados
print ("Dos números digitados: ")
print (f'{intervalo1} estão no intervalo de [0 - 25]')
print (f'{intervalo2} estão no intervalo de [26 - 50]')
print (f'{intervalo3} estão no intervalo de [51 - 75]')
print (f'{intervalo4} estão no intervalo de [76 - 100]')