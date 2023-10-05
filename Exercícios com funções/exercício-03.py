'''Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.'''

# Declara função para soma
def soma(a, b, c):
    return a + b + c

# Coleta os valores
a = int(input("Insira o valor de a: "))
b = int(input("Insira o valor de b: "))
c = int(input("Insira o valor de c: "))

# Declara variável para armazenar o resultado da função chamada
resultado = soma(a, b, c)
print(f'O resultado é: {resultado}')
