'''Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.'''

# Coleta o número
num = int(input("Insira um número inteiro: "))

# Declara função para verificar se é primo
def ePrimo(n):
    if n <= 1:
        return 'Número não é primo'
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return f'Número não é primo. É divisível por {i}'
    return 'Número é primo'

# Declara variável para armazenar o resultado e chama a função
res = ePrimo(num)

# Mostra o resultado
print(f'{num} é primo?')
print(res)