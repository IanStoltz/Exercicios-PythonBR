'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500.
'''

# Coleta o número de termos
termos = int(input("Digite o numero de termos da série de Fibonacci: "))

# Declara variáveis para iniciar geração
numero = 1
numero_anterior = 0

# Atualiza as variáveis até o valor definido e mostra resultado atual
for _ in range(termos):
    print(numero)
    aux = numero
    numero += numero_anterior
    numero_anterior = aux
    if numero >= 500:
        break
    else:
        continue