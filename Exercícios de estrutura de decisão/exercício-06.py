'''Faça um Programa que leia três números e mostre o maior deles.'''

# Coleta os números
num = float(input("Insira um número: "))
num1 = float(input("Insira outro número: "))
num2 = float(input("Insira outro número: "))

# Compara maiores menores ou iguais e mostra o resultado
if num > num1 and num > num2:
    print (f'{num} é o maior número')
elif num1 > num and num1 > num2:
    print (f'{num1} é o maior número')
elif num2 > num and num2 > num1:
    print (f'{num2} é o maior número')
else:
    print ("Os números são iguais")