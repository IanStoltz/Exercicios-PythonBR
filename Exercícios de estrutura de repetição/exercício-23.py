'''
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
'''
# Declara função para verificar se é primo
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

# Declara variável para armazenar o número de divisões
divisoes = 0

# Verifica números no intervalo especificado e adiciona na lista
for i in range(numero + 1):
    if verificar_primo(i):
        lista.append(i)
    divisoes += 1

# Mostra os resultados
print("Números primos: ", lista)
print("Número de divisões: ", divisoes)