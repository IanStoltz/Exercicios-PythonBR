'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''

# Coleta o número
num = int(input("Insira um número inteiro: "))

# Declara função para verificar se é primo
def ePrimo(n):
    if n <= 1:
        return 'Número não é primo'
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 'Número não é primo'
    return 'Número é primo'

# Declara variável para armazenar o resultado e chama a função
res = ePrimo(num)

# Mostra o resultado
print(f'{num} é primo?')
print(res)