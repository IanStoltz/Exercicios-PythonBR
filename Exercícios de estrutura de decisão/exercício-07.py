'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''

# Coleta os números e declara variável para armazenar o maior
num = float(input("Insira um número: "))
num1 = float(input("Insira outro número: "))
num2 = float(input("Insira outro número: "))
maior = num

# Compara maiores, menores ou iguais e mostra o resultado
if num1 > num and num1 > num2:
    maior = num1
elif num2 > num and num2 > num1:
    maior = num2
menor = num
if num1 < num2 and num1 < num:
    menor = num1
elif num2 < num1 and num2 < num:
    menor = num2
if num != num1 and num != num2:
    print(f'O menor número é {menor} e o maior é {maior}')
else: 
    print ("Os números são iguais")