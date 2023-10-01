'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, 
sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''

# Importa math para calcular a raiz quadrada
import math

print("Equação do segundo grau na forma: ax² + bx + c")

# Coleta o valor de A
a = int(input("Insira o valor de a: "))

# Compara o valor de A, caso seja 0, encerra o programa. Caso não, coleta os valores de B e C
if a == 0:
    print("Não é uma equação do segundo grau")
else:
    b = int(input("Insira o valor de b: "))
    c = int(input("Insira o valor de c: "))

    # Calcula o delta
    delta = (b * b) - (4 * a * c)

    # Compara o valor de delta para verificar as raízes e mostra o resultado, se existente
    if delta < 0:
        print("Não há raízes reais")
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f'Delta = 0, raiz = {raiz}')
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'x´ = {raiz1}, x´´ = {raiz2}')