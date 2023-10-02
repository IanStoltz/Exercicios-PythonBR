# Exercício repetido / enunciado diferente

'''
Encontrar números primos é uma tarefa difícil. 
Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
'''

# Declara função que verifica se é primo
def verificar_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Coleta o número
numero = int(input("Digite um número: "))

# Declara lista para armazenar os números primos
lista = []

# Verifica números no intervalo especificado e adiciona na lista
for i in range(numero + 1):
    if verificar_primo(i):
        lista.append(i)

# Mostra os resultados
print("Números primos: ", lista)