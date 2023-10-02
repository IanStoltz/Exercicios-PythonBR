'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120'''

# Coleta número de entrada e declarando variáveis
num = int(input("Insira um número para saber o fatorial: "))
resultado = 1
contagem = 1

# Incrementa a contagem e o resultado até que se atinja o número inserido
while contagem <= num:
    resultado *= contagem
    contagem += 1

# Mostra o resultado
print (f'O resultado é de: {resultado}')