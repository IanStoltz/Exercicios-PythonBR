'''
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a 
números inteiros positivos e menores que 16.
'''

# Coleta número de entrada e declara variáveis
num = int(input("Insira um número para saber o fatorial: "))
resultado = 1
contagem = 1

# Verifica se o número está dentro do intervalo permitido
while num < 0 or num >= 16:
    print("O número deve ser um inteiro positivo menor que 16.")
    num = int(input("Insira um número para saber o fatorial: "))
else:
    # Calcula o fatorial
    while contagem <= num:
        resultado *= contagem
        contagem += 1

    # Mostra o resultado
    print(f'O resultado é: {resultado}')