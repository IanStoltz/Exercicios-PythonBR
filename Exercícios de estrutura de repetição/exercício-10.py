'''Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.'''

# Coletan os números
num = int(input('Insira um número inteiro: '))
num1 = int(input('Insira outro número inteiro: '))

# Mostra os números do intervalo
if num > num1:
    for a in range(num1+1,num):
        print(a)

elif num < num1:
    for a in range(num+1,num1):
        print(a)
else:
    print('Os números são iguais.')
