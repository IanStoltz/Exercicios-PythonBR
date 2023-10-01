'''Faça um Programa que peça dois números e imprima o maior deles.'''

# Coleta os números
num = int(input("Insira um número: "))
num1 = int(input("Insira outro número: "))

# Compara quem é maior e mostra o resultado
if num > num1:
    print (f"{num} é maior que {num1}")
elif num1 > num:
    print(f"{num1} é maior que {num}")
else:
    print("Os números são iguais")
