'''Altere o programa anterior para mostrar no final a soma dos números.'''

# Coleta os números
num = int(input('Insira um número inteiro: '))
num1 = int(input('Insira outro número inteiro: '))

# Calcula a soma
soma = num + num1

# Mostra os números do intervalo
if num > num1:
    for a in range(num1+1,num):
        print(a)

elif num < num1:
    for a in range(num+1,num1):
        print(a)
else:
    print('Os números são iguais.')

# Mostra o resultado
print(f'A soma dos numeros foi de {soma}')