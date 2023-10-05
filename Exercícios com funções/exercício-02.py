# Exercício repetido
'''
Faça um programa para imprimir:

    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n

para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
'''

# Declara função que gera o resultado
def imprimir_linhas(n):
    for i in range(1, n+1):
        linha = ""
        for j in range(i):
            linha += str(i) + " "
        print(linha)

# Coleta o valor de n e chama a função para exibir o resultado
n = int(input("Digite um número inteiro: "))
imprimir_linhas(n)
